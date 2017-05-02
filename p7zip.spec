#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : p7zip
Version  : 15.14.1_src_all
Release  : 9
URL      : http://downloads.sourceforge.net/project/p7zip/p7zip/15.14.1/p7zip_15.14.1_src_all.tar.bz2
Source0  : http://downloads.sourceforge.net/project/p7zip/p7zip/15.14.1/p7zip_15.14.1_src_all.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: p7zip-bin
Requires: p7zip-doc
BuildRequires : cmake
BuildRequires : sed
BuildRequires : yasm
Patch1: build.patch
Patch2: norar.patch

%description
p7zip 15.14.1
=============
Homepage : http://p7zip.sourceforge.net/
p7zip is a port of the Windows programs 7z.exe and 7za.exe provided by 7-zip.

%package bin
Summary: bin components for the p7zip package.
Group: Binaries

%description bin
bin components for the p7zip package.


%package doc
Summary: doc components for the p7zip package.
Group: Documentation

%description doc
doc components for the p7zip package.


%prep
%setup -q -n p7zip_15.14.1
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -flto -fno-semantic-interposition "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=pgo "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=pgo "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=pgo "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=pgo "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=pgo -fprofile-correction "
make V=1  %{?_smp_mflags} all2 OPTFLAGS="$CFLAGS_GENERATE"; make V=1  %{?_smp_mflags} test ; make clean ; make V=1 %{?_smp_mflags} all2 OPTFLAGS="$CFLAGS_USE"

%install
rm -rf %{buildroot}
%make_install
## make_install_append content
rm -rf %{buildroot}/usr/man/man1
rm -rf %{buildroot}/builddir/
sed -i  "s|%{buildroot}||g" %{buildroot}/usr/bin/*
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/7z
/usr/bin/7za
/usr/libexec/p7zip/7z
/usr/libexec/p7zip/7z.so
/usr/libexec/p7zip/7zCon.sfx
/usr/libexec/p7zip/7za

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/p7zip/*
