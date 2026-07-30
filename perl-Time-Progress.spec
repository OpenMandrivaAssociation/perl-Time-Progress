%define upstream_name       Time-Progress
%define upstream_version 2.15
Name:       perl-%{upstream_name}
Version:	2.15
Release:	1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Elapsed and estimated finish time reporting
Url:        https://github.com/cade-vs/perl-time-progress
Source:     https://cpan.metacpan.org/authors/id/C/CA/CADE/Time-Progress-%{version}.tar.gz
BuildRequires:	make
BuildRequires:  perl-devel
BuildRequires:  perl(Module::Build)
BuildRoot:  %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%description
Elapsed and estimated finish time reporting.

%prep
%setup -q -n %{upstream_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/
make

%check
make test

%install
rm -rf %buildroot
make install DESTDIR=${RPM_BUILD_ROOT}
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Time/Progress.pm
%{_mandir}/man3/*


