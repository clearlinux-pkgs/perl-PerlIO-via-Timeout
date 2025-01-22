#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-PerlIO-via-Timeout
Version  : 0.32
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAMS/PerlIO-via-Timeout-0.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAMS/PerlIO-via-Timeout-0.32.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libperlio-via-timeout-perl/libperlio-via-timeout-perl_0.32-1.debian.tar.xz
Summary  : 'a PerlIO layer that adds read & write timeout to a handle'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-PerlIO-via-Timeout-license = %{version}-%{release}
Requires: perl-PerlIO-via-Timeout-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Test::SharedFork)
BuildRequires : perl(Test::TCP)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution PerlIO-via-Timeout,
version 0.32:
a PerlIO layer that adds read & write timeout to a handle

%package dev
Summary: dev components for the perl-PerlIO-via-Timeout package.
Group: Development
Provides: perl-PerlIO-via-Timeout-devel = %{version}-%{release}
Requires: perl-PerlIO-via-Timeout = %{version}-%{release}

%description dev
dev components for the perl-PerlIO-via-Timeout package.


%package license
Summary: license components for the perl-PerlIO-via-Timeout package.
Group: Default

%description license
license components for the perl-PerlIO-via-Timeout package.


%package perl
Summary: perl components for the perl-PerlIO-via-Timeout package.
Group: Default
Requires: perl-PerlIO-via-Timeout = %{version}-%{release}

%description perl
perl components for the perl-PerlIO-via-Timeout package.


%prep
%setup -q -n PerlIO-via-Timeout-0.32
cd %{_builddir}
tar xf %{_sourcedir}/libperlio-via-timeout-perl_0.32-1.debian.tar.xz
cd %{_builddir}/PerlIO-via-Timeout-0.32
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/PerlIO-via-Timeout-0.32/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-PerlIO-via-Timeout
cp %{_builddir}/PerlIO-via-Timeout-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-PerlIO-via-Timeout/278dd1dba8bcbc0a77f47b72c9c54bec445a356c || :
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-PerlIO-via-Timeout/a437ddedbd1a6081def9aceff2e815fd555b622a || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/PerlIO::via::Timeout.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-PerlIO-via-Timeout/278dd1dba8bcbc0a77f47b72c9c54bec445a356c
/usr/share/package-licenses/perl-PerlIO-via-Timeout/a437ddedbd1a6081def9aceff2e815fd555b622a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
