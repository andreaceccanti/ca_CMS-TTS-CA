%global ca_name CMS-TTS-CA
%global ca_hash ff3538fd
%global ca_hash_old aa617f76

Name: ca_%{ca_name}
Version: 0.1.0
Release: 1%{?dist}
Summary: The CMS TTS CA

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
%setup -q

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates

install -m 644 -p %{ca_name}.* $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates
ln -s %{ca_name}.pem $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash}.0
ln -s %{ca_name}.pem $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash_old}.0
ln -s %{ca_name}.signing_policy $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash}.signing_policy
ln -s %{ca_name}.signing_policy $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash_old}.signing_policy
ln -s %{ca_name}.namespaces $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash}.namespaces
ln -s %{ca_name}.namespaces $RPM_BUILD_ROOT%{_sysconfdir}/grid-security/certificates/%{ca_hash_old}.namespaces

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/grid-security/certificates/*

%changelog
* Mon Apr 05 2017 Andrea Ceccanti <andrea.ceccanti at cnaf.infn.it> - 0.1.0-1
- First packaging 
