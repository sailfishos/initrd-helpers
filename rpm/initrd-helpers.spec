Name:       initrd-helpers
Summary:    Helper scripts and tools for init ramdisks
Version:    0.0.1
Release:    1
Group:      System/Boot
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz

Requires:  btrfs

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
mkdir -p %{buildroot}/sbin/
install -D -m 755 btrfs-mount-repair %{buildroot}/sbin/btrfs-mount-repair

%files
%defattr(-,root,root,-)
/sbin/btrfs-mount-repair

%doc LICENSE README



