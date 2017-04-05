Name: ca_CMS-TTS-CA
Version: 0.1.0
Release: 1%{?dist}
Summary: 

Group: Security/Certificates
License: ASL 2.0
URL: https://github.com/andreaceccanti/tts-ca

Source: %{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is the trust anchor for the authority CMS-TTS-CA.
You should install this package if you want to trust the identity
assertions issued by the CMS-TTS-CA.

%prep
%setup -c 

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates

install -m 644 -p %{name}.* $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
install -m 644 -p *.0 *.r0 *.signing_policy *.namespaces $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/certificates/*

%changelog
* Mon Apr 05 2017 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 0.1.0-1
- First packaging 
