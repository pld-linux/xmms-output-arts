Summary:	Output plugin for XMMS for use with the aRts sound server
Summary(es):	Plugin de salida para XMMS para uso con el paquete aRts
Summary(pl):	Wtyczka dla XMMS odtwarzaj±ca przez aRts
Summary(pt_BR):	Plugin de saída para o XMMS para uso com o servidor de som aRts
Name:		xmms-output-arts
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://havardk.xmms.org/plugins/arts_output/arts_output-%{version}.tar.gz
# Source0-md5: 6d028255ed86e37211bbda0122c14483
URL:		http://havardk.xmms.org/plugins/arts_output/
BuildRequires:	artsc-devel >= 1.0.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%setup -q -n arts_output-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{xmms_output_plugindir}/*
%attr(755,root,root) %{_bindir}/*
