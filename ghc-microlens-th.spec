# generated by cabal-rpm-2.0.9
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name microlens-th
%global pkgver %{pkg_name}-%{version}

%bcond_without tests

Name:           ghc-%{pkg_name}
Version:        0.4.3.9
Release:        1%{?dist}
Summary:        Automatic generation of record lenses for microlens

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-transformers-prof
%if %{with tests}
BuildRequires:  ghc-tagged-devel
%endif
# End cabal-rpm deps

%description
This package lets you automatically generate lenses for data types; code was
extracted from the lens package, and therefore generated lenses are fully
compatible with ones generated by lens (and can be used both from lens and
microlens).

This package is a part of the <http://hackage.haskell.org/package/microlens
microlens> family; see the readme <https://github.com/monadfix/microlens#readme
on Github>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 0.4.3.9-1
- update to 0.4.3.9

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Jens Petersen <petersen@redhat.com> - 0.4.3.5-1
- update to 0.4.3.5

* Thu Feb 20 2020 Jens Petersen <petersen@redhat.com> - 0.4.2.3-6
- enable tests
- revised .cabal

* Wed Feb 19 2020 Jens Petersen <petersen@redhat.com> - 0.4.2.3-5
- refresh to cabal-rpm-2.0.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 02 2019 Jens Petersen <petersen@redhat.com> - 0.4.2.3-3
- add doc and prof subpackages (cabal-rpm-1.0.0)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 0.4.2.3-1
- update to 0.4.2.3

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 0.4.1.3-4
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.4.1.3-1
- update to 0.4.1.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Jens Petersen <petersen@redhat.com> - 0.4.1.1-2
- rebuild

* Sat Jul 22 2017 Fedora Haskell SIG <haskell@lists.fedoraproject.org> - 0.4.1.1-1
- spec file generated by cabal-rpm-0.11
