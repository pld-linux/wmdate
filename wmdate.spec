Summary:	wmdate - date-display utility for X11
Summary(pl):	wmdate - program dla X11 wy¶wietlaj±cy datê
Name:		wmdate
Version:	0.7
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/%{name}-%{version}.tar.gz
Source1:	wmdate.desktop
URL:		http://wit401310.student.utwente.nl/apps/wmdate.html
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	libdockapp-devel >= 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmDate is a date-display utility designed for WindowMaker Dock. It was
originally based on the displaying lay-out of asclock (which in turn is
based on the time-display utility used in NeXTStep).

%description -l pl
wmDate jest dokowalnym apletem dla WindowMakera wy¶wietlaj±cym datê.
Jego wygl±d oparty jest na programie asclock (który z kolei jest oparty
na wy¶wietlaj±cym czas programie dla NextStep).

%prep
%setup -q

%build
xmkmf
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"
strip wmdate

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf README Changelog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changelog}.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_applnkdir}/DockApplets/%{name}.desktop
