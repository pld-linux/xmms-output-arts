Summary:	aRts output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS odtwarzająca przez aRts
Name:  		xmms-output-arts
Version: 	0.4
Release: 	1
Copyright: 	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
URL: 		http://home.earthlink.net/~bheath/xmms-arts/
Source0:	http://home.earthlink.net/~bheath/xmms-arts/xmmsarts-%{version}.tar.gz
Requires:	xmms
BuildRequires:	arts-devel
BuildRequires:	xmms-devel
buildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
This plugin allows xmms to play sounds though aRts sound servers. This is a
must-have for KDE2 users, because aRts, which is by default started in this
environment, uses DSP, thus preventing oss-plugin from working.

%description -l pl
Ta wtyczka pozwala xmms'owi odtwarzać muzykę poprzez serwer aRts. Obowiązkowy
pakiet dla użytkowników KDE2, ponieważ aRts, domyślnie uruchamiany w tym
środowisku, używa DSP tym samym uniemożliwiając działanie wtyczce OSS.

%prep
%setup -q -n xmms-arts-%{version}

%build
export CFLAGS="-I/usr/X11R6/include"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip README NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xmms/Output/*
%doc *.gz
