# TODO
# - fix kopete-tool-{avdeviceconfig,smpppdcs} summaries/descriptions (copy-pastos!)
# - BR phonon-devel
# - FILES update
#
# Conditional build:
#
%define		_state		stable
%define		orgname		kppp
%define		qtver		4.8.3

Summary:	KDE PPP dialer
Summary(pl.UTF-8):	Program do połączeń modemowych dla KDE
Summary(pt_BR.UTF-8):	O discador para Internet
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	2899d881b8fff48ba3122204f15bf1dc
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtOpenGL-devel >= %{qtver}
BuildRequires:	QtScript-devel >= %{qtver}
BuildRequires:	QtSql-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	QtTest-devel >= %{qtver}
BuildRequires:	QtWebKit-devel >= %{qtver}
BuildRequires:	alsa-lib-devel
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	giflib-devel
BuildRequires:	gmp-devel
BuildRequires:	gpgme-devel
BuildRequires:	jasper-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	kde4-kdebase-workspace-devel >= 4.11.4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	libgadu-devel >= 1.8.0
BuildRequires:	libidn-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libktorrent-devel >= 1.0.2
BuildRequires:	libmms-devel
BuildRequires:	libmsn-devel >= 4.1
BuildRequires:	libotr-devel >= 4.0.0
BuildRequires:	libv4l-devel >= 0.5.8
BuildRequires:	libvncserver-devel
BuildRequires:	libxml2-progs
BuildRequires:	libxslt-devel >= 1.0.7
BuildRequires:	meanwhile-devel >= 1.0.1
BuildRequires:	mediastreamer-devel >= 2.3.0
BuildRequires:	msilbc-devel >= 2.0.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	ortp-devel >= 0.16.1-3
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	qca-devel >= 2.0
BuildRequires:	qimageblitz-devel >= 0.0.6
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-desktop-ontologies-devel >= 0.5
BuildRequires:	soprano-devel >= 2.4.64
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRequires:	strigi-devel >= 0.7.2
BuildRequires:	telepathy-qt4-devel >= 0.9.0
BuildRequires:	xmms-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXtst-devel
Obsoletes:	kde4-kdenetwork-kppp
Conflicts:	kde4-kdenetwork
Requires:	kde4-kdebase >= %{version}
Requires:	ppp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KPPP is a dialer and front end for pppd. It allows for interactive
script generation and network setup. It will automate the dialing in
process to your ISP while letting you conveniently monitor the entire
process.

Once connected KPPP will provide a rich set of statistics and keep
track of the time spent online for you.

A built-in terminal and script generator will enable you to set up
your connection with ease. You will no longer need an additional
terminal program such as seyon or minicom to test and setup your
connection.

KPPP features elaborate phone cost accounting, which enables you to
easily track your online costs.

%description -l pl.UTF-8
KPPP to program do nawiązywania połączeń modemowych i frontend dla
pppd. Pozwala na interaktywne generowanie skryptów i konfiguracji
sieci. Automatyzuje proces dzwonienia do swojego ISP umożliwiając
jednocześnie wygodne monitorowanie całego procesu.

Po połączeniu KPPP udostępnia bogate statystyki i śledzi czas spędzony
online.

Wbudowany terminal i generator skryptów umożliwia łatwe
skonfigurowanie połączenia. Nie trzeba już dodatkowego programu
terminalowego, takiego jak seyon czy minicom, do testowania i
ustawiania połączenia.

KPPP ma wypracowane naliczanie kosztów telefonów, pozwalające łatwo
śledzić koszt czasu online.

%description -l pt_BR.UTF-8
O discador para Internet.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DMOZPLUGIN_INSTALL_DIR=%{_browserpluginsdir} \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

%find_lang	%{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kppplogview
%attr(755,root,root) %{_bindir}/kppp
%{_datadir}/apps/kppp
%{_datadir}/dbus-1/interfaces/org.kde.kppp.xml
%{_desktopdir}/kde4/Kppp.desktop
%{_desktopdir}/kde4/kppplogview.desktop
%{_iconsdir}/*/*/*/kppp.png
