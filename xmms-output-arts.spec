Summary:	Output plugin for XMMS for use with the aRts sound server
Summary(es):	Plugin de salida para XMMS para uso con el paquete aRts
Summary(pl):	Wtyczka dla XMMS odtwarzaj±ca przez aRts
Summary(pt_BR):	Plugin de saída para o XMMS para uso com o servidor de som aRts
Name:		xmms-output-arts
Version:	0.4
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://home.earthlink.net/~bheath/xmms-arts/xmmsarts-%{version}.tar.gz
Patch0:		%{name}-nocmallocc.patch
URL:		http://home.earthlink.net/~bheath/xmms-arts/
BuildRequires:	arts-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description 
This plugin allows xmms to play sounds though aRts sound servers. This
is a must-have for KDE2 users, because aRts, which is by default
started in this environment, uses DSP, thus preventing oss-plugin from
working.

%description -l es
Plugin de salida para XMMS para uso con el paquete aRts.

%description -l pl
Ta wtyczka pozwala xmms-owi odtwarzaæ muzykê poprzez serwer aRts.
Obowi±zkowy pakiet dla u¿ytkowników KDE2, poniewa¿ aRts, domy¶lnie
uruchamiany w tym ¶rodowisku, u¿ywa DSP tym samym uniemo¿liwiaj±c
dzia³anie wtyczce OSS.

%description -l pt_BR
Plugin de saída para o XMMS trabalhar com o servidor de som aRts.

%prep
%setup -q -n xmms-arts-%{version}
%patch0 -p1

%build
CFLAGS="-I%{_includedir}"
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
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
