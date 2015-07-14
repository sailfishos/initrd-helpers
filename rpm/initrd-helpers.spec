Name:       initrd-helpers
Summary:    Helper scripts and tools for init ramdisks
Version:    0.0.1
Release:    1
Group:      System/Boot
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz

Requires:  btrfs-progs
Requires:  findutils
Requires:  e2fsprogs
Requires:  cryptsetup-luks
Requires:  lvm2

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}


%build

%install
mkdir -p %{buildroot}/sbin/
install -D -m 755 btrfs-mount-repair %{buildroot}/sbin/btrfs-mount-repair
install -D -m 755 factory-reset-lvm %{buildroot}/sbin/factory-reset-lvm
install -D -m 755 find-mmc-bypartlabel %{buildroot}/sbin/find-mmc-bypartlabel
install -D -m 755 lvm-luks-convert %{buildroot}/sbin/lvm-luks-convert

%files
%defattr(-,root,root,-)
/sbin/btrfs-mount-repair
/sbin/factory-reset-lvm
/sbin/find-mmc-bypartlabel
/sbin/lvm-luks-convert

%doc LICENSE README



