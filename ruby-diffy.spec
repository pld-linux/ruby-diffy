#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	diffy
Summary:	Easy Diffing in Ruby
Name:		ruby-%{pkgname}
Version:	3.0.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	073f71cb2d294e03235ecbe527ec43a3
Patch0:		diff-path.patch
URL:		https://github.com/samg/diffy
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake < 0.10
BuildRequires:	ruby-rake >= 0.9.2
BuildRequires:	ruby-rspec < 3
BuildRequires:	ruby-rspec >= 2.0
%endif
Requires:	diffutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A convenient way to diff string in Ruby.

Provides a convenient way to generate a diff from two strings or
files. Instead of reimplementing the LCS diff algorithm Diffy uses
battle tested Unix diff to generate diffs, and focuses on providing a
convenient interface, and getting out of your way.

Supported Formats
- text - Plain text output
- color - ANSI colorized text suitable for use in a terminal
- html - HTML output. Since version 2.0 this format does inline
  highlighting of the character changes between lines.
- html_simple - HTML output without inline highlighting. This may be
  useful in situations where high performance is required or simpler
  output is desired.

%prep
%setup -q -n %{pkgname}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG CONTRIBUTORS LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
