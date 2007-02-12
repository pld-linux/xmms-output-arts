Summary:	Output plugin for XMMS for use with the aRts sound server
Summary(es.UTF-8):	Plugin de salida para XMMS para uso con el paquete aRts
Summary(pl.UTF-8):	Wtyczka wyjściowa dla XMMS-a odtwarzająca przez aRts
Summary(pt_BR.UTF-8):	Plugin de saída para o XMMS para uso com o servidor de som aRts
Name:		xmms-output-arts
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://havardk.xmms.org/plugins/arts_output/arts_output-%{version}.tar.gz
# Source0-md5:	6d028255ed86e37211bbda0122c14483
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
This plugin allows XMMS to play sounds though aRts sound servers. This
is a must-have for KDE users, because aRts, which is by default
started in this environment, uses DSP, thus preventing oss-plugin from
working.

%description -l es.UTF-8
Plugin de salida para XMMS para uso con el paquete aRts.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać muzykę poprzez serwer aRts.
Obowiązkowy pakiet dla użytkowników KDE, ponieważ aRts, domyślnie
uruchamiany w tym środowisku, używa DSP tym samym uniemożliwiając
działanie wtyczce OSS.

%description -l pt_BR.UTF-8
Plugin de saída para o XMMS trabalhar com o servidor de som aRts.

%prep
%setup -q -n arts_output-%{version}

%build
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

rm -f $RPM_BUILD_ROOT%{xmms_output_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{xmms_output_plugindir}/*.so
