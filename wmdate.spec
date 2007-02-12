Summary:	wmdate - date-display utility for X11
Summary(pl.UTF-8):   wmdate - program dla X11 wyświetlający datę
Name:		wmdate
Version:	0.7
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://solfertje.student.utwente.nl/~dalroi/wmdate/files/%{name}-%{version}.tar.gz
# Source0-md5:	967a20599124da13c876d12cfe08e3a5
Source1:	%{name}.desktop
Patch0:		%{name}-ComplexProgramTargetNoMan.patch
URL:		http://solfertje.student.utwente.nl/~dalroi/wmdate/
BuildRequires:	XFree86-devel
BuildRequires:	libdockapp-devel >= 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmDate is a date-display utility designed for WindowMaker Dock. It was
originally based on the displaying lay-out of asclock (which in turn
is based on the time-display utility used in NeXTStep).

%description -l pl.UTF-8
wmDate jest dokowalnym apletem dla WindowMakera wyświetlającym datę.
Jego wygląd oparty jest na programie asclock (który z kolei jest
oparty na wyświetlającym czas programie dla NextStep).

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets \
	$RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
