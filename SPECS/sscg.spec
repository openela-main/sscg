%global provider        github
%global provider_tld    com
%global project sgallagher
%global repo sscg
# https://github.com/sgallagher/sscg
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}


Name:           sscg
Version:        3.0.0
Release:        7%{?dist}
Summary:        Simple SSL certificate generator

License:        GPLv3+ with exceptions
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/releases/download/%{repo}-%{version}/%{repo}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  libtalloc-devel
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  libpath_utils-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  help2man


Patch: 0001-Drop-usage-of-ERR_GET_FUNC.patch
Patch: 0002-Correct-certificate-lifetime-calculation.patch
Patch: 0003-Truncate-IP-address-in-SAN.patch
Patch: 0004-dhparams-don-t-fail-if-default-file-can-t-be-created.patch
Patch: 0005-dhparams-Fix-the-FIPS_mode-call-for-OpenSSL-3.0.patch

%description
A utility to aid in the creation of more secure "self-signed"
certificates. The certificates created by this tool are generated in a
way so as to create a CA certificate that can be safely imported into a
client machine to trust the service certificate without needing to set
up a full PKI environment and without exposing the machine to a risk of
false signatures from the service certificate.

%prep
%autosetup -p1


%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test -t 10

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Fri Dec 02 2022 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-6
- Use EVP_default_properties_is_fips_enabled() on OpenSSL 3.0
- Related: rhbz#2083879

* Mon Nov 28 2022 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-6
- Don't fail if default dhparams file can't be created
- Resolves: rhbz#2149064

* Wed Mar 09 2022 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-5
- Handle IP addresses in subjectAlternativeName correctly
- Resolves: rhbz#2061923

* Fri Oct 29 2021 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-4
- Correct certificate lifetime calculation
- Resolves: rhbz#2017667

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 3.0.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Sat Aug 07 2021 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-2
- Drop usage of removed macro ERR_GET_FUNC()
- Related: rhbz#1964837

* Wed Jul 21 2021 Stephen Gallagher <sgallagh@redhat.com> - 3.0.0-1
- Release 3.0.0
- Support for OpenSSL 3.0
- Support for outputting named Diffie-Hellman parameter groups
- Support for CentOS Stream 9
- Resolves: rhbz#1984468

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.6.2-8
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Wed May 26 2021 Stephen Gallagher <sgallagh@redhat.com> - 2.6.2-7
- OpenSSL 3.0 compatibility: fix RSA key-generation test
- Resolves: rhbz#1964837

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.6.2-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Mar 17 2021 Stephen Gallagher <sgallagh@redhat.com> - 2.6.2-5
- Fixing incorrect license declaration

* Wed Mar 17 2021 Stephen Gallagher <sgallagh@redhat.com> - 2.6.2-4
- Updating to rebuild against the latest glibc

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.6.2-1
- Update to 2.6.2
- Handle very short and very long passphrases properly (fixes rhbz#1850183)
- Drop upstreamed patch

* Thu Apr 30 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.6.1-4
- Rebuild with corrected ELN macro definitions

* Thu Apr 30 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.6.1-3
- Don't bother running clang-format in the RPM build
- Lengthen the test timeout so ARM tests pass

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Stephen Gallagher <sgallagh@redhat.com> - 2.6.1-1
- Bugfixes from upstream

* Fri Dec 13 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.6.0-2
- Fix incorrect help description for --client-key-file

* Fri Dec 13 2019 Stephen Gallagher <sgallagh@redhat.com> - 2.6.0-1
- Update to 2.6.0
- Can now generate an empty CRL file.
- Can now create and store a Diffie-Hellman parameters (dhparams) file.
- Support for setting a password on private keys.
- Support for generating a client authentication certificate and key.
- Better support for OpenSSL 1.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.5.1-1
- Update to 2.5.1
- Fixes discovered by automated testing.

* Wed Nov 28 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.5.0-1
- Update to 2.5.0
- Auto-detect the hash algorithm to use by default.

* Tue Nov 27 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.4.0-1
- Update to 2.4.0
- Autodetect the minimum key strength from the system security level.
- Disallow setting a key strength below the system minimum.

- Drop upstreamed patches

* Mon Sep 17 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.3.3-4
- Add a manpage.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.3.3-1
- Update to 2.3.3
- Do not overwrite destination files without --force

* Thu Jan 25 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.3.2-1
- Update to 2.3.2
- Properly support hostnames up to 64 characters
- Resolves: rhbz#1535537

* Tue Jan 02 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.3.1-2
- Skip tests on 32-bit ARM for now

* Tue Jan 02 2018 Stephen Gallagher <sgallagh@redhat.com> - 2.3.1-1
- Update to 2.3.1
- Bundle popt 1.16 on older releases like EPEL.

* Mon Dec 18 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.3.0-1
- Update to 2.3.0
- Switch to meson build system
- Add support for non-DNS subjectAlternativeName values (issue #4)

* Thu Sep 21 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.2.0-1
- Reorder combined PEM file
- Resolves: RHBZ#1494208

* Wed Sep 20 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.1.0-1
- Add --email argument for setting emailAddress in the issuer

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.4-2
- Bump release to perform taskotron tests

* Tue Mar 21 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.4-1
- Update to 2.0.4
- Addresses a potential race-condition when the key and certificate share the
  same file.

* Wed Mar 08 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.3-1
- Update to 2.0.3
- Adds support for setting the file mode on the output certificates
  and keys.

* Fri Mar 03 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.2-1
- Update to 2.0.2
- Always run with umask(077)

* Fri Mar 03 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.1-1
- Update to 2.0.1
- Fix an issue with passing certificate lifetime explicitly

* Thu Feb 16 2017 Stephen Gallagher <sgallagh@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 16 2017 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-6
- Exclude PPC64 from the build since it doesn't support linking to OpenSSL

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-4
- Use compat-openssl10-devel on F26+

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue May 31 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-2
- Debundle spacelog

* Wed May 25 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Add support for signing service keys with an existing CA

* Wed May 25 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.4-1
- Add support for exporting the CA private key
- Fix incorrect output from -version
- Add README.md

* Tue May 24 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.3-1
- Only sign certificates after all extensions have been added

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.2-1
- Generate x509v3 certificates

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-1
- Fix issue with temporary file creation

* Mon May 23 2016 Stephen Gallagher <sgallagh@redhat.com> - 1.0.0-1
- New upstream release 1.0.0
- Rewritten in Go
- Runtime depends only on OpenSSL, no more Python
- Support for writing certificate and key in a single file

* Wed May 18 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.4.1-4
- Add requirement on python-setuptools

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Stephen Gallagher <sgallagh@redhat.com> 0.4.1-1
- Change default CA location to match service certificate
- Improve error handling

* Tue Mar 24 2015 Stephen Gallagher <sgallagh@redhat.com> 0.4.0-1
- Spec file cleanups
- PEP8 Cleanups
- Make location arguments optional

* Mon Mar 23 2015 Stephen Gallagher <sgallagh@redhat.com> 0.3.0-1
- Rename to sscg
- Only build with default python interpreter

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2.1-1
- Include the LICENSE file in the tarball

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2-2
- Include the license in the build RPMs

* Tue Mar 17 2015 Stephen Gallagher <sgallagh@redhat.com> 0.2-1
- Add support for namedConstraints
- Add support for subjectAltNames
- Fix packaging issues from Fedora package review

* Mon Mar 16 2015 Stephen Gallagher <sgallagh@redhat.com> 0.1-2
- Update BuildRequires

* Mon Mar 16 2015 Stephen Gallagher <sgallagh@redhat.com> 0.1-1
- First packaging

