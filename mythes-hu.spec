Name: mythes-hu
Summary: Hungarian thesaurus
%define upstreamid 20101019
Version: 0.%{upstreamid}
Release: 6%{?dist}
Source: http://extensions.services.openoffice.org/e-files/1283/9/dict-hu.oxt
Group: Applications/Text
URL: http://extensions.services.openoffice.org/project/hu_dicts
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#bundled but unused spell-checking stuff is under GPLv2+ or LGPLv2+ or MPLv1.1
#base for bundled but unused hyphenation stuff is under GPLv2
#additional patch to unused hyphenation stuff is MPL/GPL/LGPL
License: GPLv2+ and (GPLv2+ or LGPLv2+ or MPLv1.1) and GPLv2 and (GPL+ or LGPLv2+ or MPLv1.1)
BuildArch: noarch
Requires: mythes

%description
Hungarian thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_hu_HU_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_hu_HU_v2.txt
%{_datadir}/mythes/*

%changelog
* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20101019-6
- Resolves: rhbz#905964 nemeth hates version control, or versions :-)

* Tue Nov 06 2012 Caolán McNamara <caolanm@redhat.com> - 0.20101019-5
- clarify license

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101019-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Oct 20 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101019-1
- latest version

* Sat May 15 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100512-1
- latest version

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100329-2
- mythes now owns /usr/share/mythes

* Wed Mar 31 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100329-1
- latest version

* Sun Feb 14 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100213-1
- latest version

* Fri Sep 18 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090918-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090203-1
- initial version
