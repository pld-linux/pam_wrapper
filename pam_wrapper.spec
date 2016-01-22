Summary:	PAM wrapper library - tool to test PAM applications and modules
Summary(pl.UTF-8):	Biblioteka obudowująca PAM - narzędzie do testowania aplikacji i modułów PAM
Name:		pam_wrapper
Version:	1.0.1
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://www.samba.org/ftp/cwrap/%{name}-%{version}.tar.gz
# Source0-md5:	3336b38247d67a60b32b033769cd480f
URL:		http://cwrap.org/pam_wrapper.html
BuildRequires:	cmake >= 2.8.0
# for tests
#BuildRequires:	cmocka-devel
BuildRequires:	pam-devel
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	pam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This component of cwrap allows you to either test your PAM (Linux-PAM
and OpenPAM) application or module. For testing PAM applications there
is a simple PAM module called pam_matrix. If you plan to test a PAM
module you can use the pamtest library. It simplifies testing of
modules. You can combine it with the cmocka unit testing framework or
you can use the provided Python bindings to write tests for your
module in Python.

%description -l pl.UTF-8
Ten komponent cwrap pozwala na testowanie aplikacji lub modułów PAM
(Linux-PAM lub OpenPAM). Do testowania aplikacji PAM służy prosty
moduł PAM o nazwie pam_matrix. Do testowania modułów służy biblioteka
pamtest, upraszczająca testowanie. Można łączyć ją ze szkieletem
testów jednostkowych cmocka, albo użyć dostarczonych wiązań Pythona do
pisania własnych testów modułu w Pythonie.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libpam_wrapper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpam_wrapper.so.0
%attr(755,root,root) %{_libdir}/libpam_wrapper.so
%attr(755,root,root) %{_libdir}/libpamtest.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpamtest.so.0
%attr(755,root,root) %{_libdir}/libpamtest.so
%dir %{_libdir}/pam_wrapper
%attr(755,root,root) %{_libdir}/pam_wrapper/pam_get_items.so
%attr(755,root,root) %{_libdir}/pam_wrapper/pam_matrix.so
%attr(755,root,root) %{_libdir}/pam_wrapper/pam_set_items.so
%attr(755,root,root) %{py_sitedir}/pypamtest.so
%{_includedir}/libpamtest.h
%{_pkgconfigdir}/libpamtest.pc
%{_pkgconfigdir}/pam_wrapper.pc
%{_libdir}/cmake/libpamtest
%{_libdir}/cmake/pam_wrapper
%{_mandir}/man1/pam_wrapper.1*
%{_mandir}/man8/pam_get_items.8*
%{_mandir}/man8/pam_matrix.8*
%{_mandir}/man8/pam_set_items.8*
