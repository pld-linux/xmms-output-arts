Summary:	aRts output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS odtwarzaj±ca przez aRts
Name:		xmms-output-arts
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
URL:		http://home.earthlink.net/~bheath/xmms-arts/
Source0:	http://home.earthlink.net/~bheath/xmms-arts/xmmsarts-%{version}.tar.gz
Requires:	xmms
BuildRequires:	arts-devel
BuildRequires:	xmms-devel
buildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
This plugin allows xmms to play sounds though aRts sound servers. This
is a must-have for KDE2 users, because aRts, which is by default
started in this environment, uses DSP, thus preventing oss-plugin from
working.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê poprzez serwer aRts.
Obowi±zkowy pakiet dla u¿ytkowników KDE2, poniewa¿ aRts, domy¶lnie
uruchamiany w tym ¶rodowisku, u¿ywa DSP tym samym uniemo¿liwiaj±c
dzia³anie wtyczce OSS.

%prep
%setup -q -n xmms-arts-%{version}

%build
CFLAGS="-I%{_includedir}"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/*
%doc *.gz
