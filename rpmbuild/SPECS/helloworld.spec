Name: helloworld
Version: 1.0
Release: 1%{?dist}
Summary: Print Hello World!
License: BSD
URL: http://example.com

%description
Print Hello World!

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 helloworld %{buildroot}/usr/bin/helloworld

%files
/usr/bin/helloworld

%changelog
