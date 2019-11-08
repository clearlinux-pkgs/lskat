#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : lskat
Version  : 19.08.3
Release  : 15
URL      : https://download.kde.org/stable/applications/19.08.3/src/lskat-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/lskat-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/lskat-19.08.3.tar.xz.sig
Summary  : Lieutenant Skat is a fun and engaging card game for two players
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: lskat-bin = %{version}-%{release}
Requires: lskat-data = %{version}-%{release}
Requires: lskat-license = %{version}-%{release}
Requires: lskat-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
GENERAL NOTE:
https://games.kde.org/

%package bin
Summary: bin components for the lskat package.
Group: Binaries
Requires: lskat-data = %{version}-%{release}
Requires: lskat-license = %{version}-%{release}

%description bin
bin components for the lskat package.


%package data
Summary: data components for the lskat package.
Group: Data

%description data
data components for the lskat package.


%package doc
Summary: doc components for the lskat package.
Group: Documentation

%description doc
doc components for the lskat package.


%package license
Summary: license components for the lskat package.
Group: Default

%description license
license components for the lskat package.


%package locales
Summary: locales components for the lskat package.
Group: Default

%description locales
locales components for the lskat package.


%prep
%setup -q -n lskat-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573191508
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573191508
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lskat
cp %{_builddir}/lskat-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/lskat/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8
cp %{_builddir}/lskat-19.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/lskat/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/lskat-19.08.3/COPYING.LIB %{buildroot}/usr/share/package-licenses/lskat/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd
%find_lang lskat

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lskat

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.lskat.desktop
/usr/share/icons/hicolor/128x128/apps/lskat.png
/usr/share/icons/hicolor/16x16/apps/lskat.png
/usr/share/icons/hicolor/22x22/apps/lskat.png
/usr/share/icons/hicolor/32x32/apps/lskat.png
/usr/share/icons/hicolor/48x48/apps/lskat.png
/usr/share/icons/hicolor/64x64/apps/lskat.png
/usr/share/kxmlgui5/lskat/lskatui.rc
/usr/share/lskat/grafix/blue.desktop
/usr/share/lskat/grafix/blue.rc
/usr/share/lskat/grafix/blue.svg
/usr/share/lskat/grafix/egyptian.desktop
/usr/share/lskat/grafix/egyptian.rc
/usr/share/lskat/grafix/egyptian.svg
/usr/share/lskat/grafix/oxygen.desktop
/usr/share/lskat/grafix/oxygen.rc
/usr/share/lskat/grafix/oxygen.svg
/usr/share/metainfo/org.kde.lskat.appdata.xml
/usr/share/qlogging-categories5/lskat.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/cs/lskat/index.cache.bz2
/usr/share/doc/HTML/cs/lskat/index.docbook
/usr/share/doc/HTML/de/lskat/index.cache.bz2
/usr/share/doc/HTML/de/lskat/index.docbook
/usr/share/doc/HTML/en/lskat/index.cache.bz2
/usr/share/doc/HTML/en/lskat/index.docbook
/usr/share/doc/HTML/en/lskat/lskat_screen_01.png
/usr/share/doc/HTML/es/lskat/index.cache.bz2
/usr/share/doc/HTML/es/lskat/index.docbook
/usr/share/doc/HTML/et/lskat/index.cache.bz2
/usr/share/doc/HTML/et/lskat/index.docbook
/usr/share/doc/HTML/fr/lskat/index.cache.bz2
/usr/share/doc/HTML/fr/lskat/index.docbook
/usr/share/doc/HTML/fr/lskat/lskat_screen_01.png
/usr/share/doc/HTML/it/lskat/index.cache.bz2
/usr/share/doc/HTML/it/lskat/index.docbook
/usr/share/doc/HTML/nl/lskat/index.cache.bz2
/usr/share/doc/HTML/nl/lskat/index.docbook
/usr/share/doc/HTML/pt/lskat/index.cache.bz2
/usr/share/doc/HTML/pt/lskat/index.docbook
/usr/share/doc/HTML/pt_BR/lskat/index.cache.bz2
/usr/share/doc/HTML/pt_BR/lskat/index.docbook
/usr/share/doc/HTML/ru/lskat/index.cache.bz2
/usr/share/doc/HTML/ru/lskat/index.docbook
/usr/share/doc/HTML/sv/lskat/index.cache.bz2
/usr/share/doc/HTML/sv/lskat/index.docbook
/usr/share/doc/HTML/uk/lskat/index.cache.bz2
/usr/share/doc/HTML/uk/lskat/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lskat/ba8966e2473a9969bdcab3dc82274c817cfd98a1
/usr/share/package-licenses/lskat/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/lskat/fafaf6b2753f82aa8df1d206d6b76c2241c2dfa8

%files locales -f lskat.lang
%defattr(-,root,root,-)

