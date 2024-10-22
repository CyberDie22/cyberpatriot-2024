# 1.1.1.1 Ensure cramfs kernel module is not available (Automated)

### Profile Applicability:

 • Level 1 - Server

 • Level 1 - Workstation

 Description:

 The cramfs filesystem type is a compressed read-only Linux filesystem embedded in small footprint systems. A cramfs image can be used without having to first decompress the image.

 Rationale:

 Removing support for unneeded filesystem types reduces the local attack surface of the system. If this filesystem type is not needed, disable it.

 Audit:

 Run the following script to verify the cramfs module is disabled: -IF- the module is available in the running kernel:

#### • An entry including /bin/true or /bin/false exists in a file within the
```
    /etc/modprobe.d/ directory

 • The module is deny listed in a file within the /etc/modprobe.d/ directory

 • The module is not loaded in the kernel

### -IF- available in ANY installed kernel:

#### • The module is deny listed in a file within the /etc/modprobe.d/ directory

### -IF- the kernel module is not available on the system, or pre-compiled into the kernel:

#### • No additional configuration is necessary

 Page 21

```

-----

```
#!/usr/bin/env bash
{
  l_output="" l_output2="" l_output3="" l_dl="" # Unset output variables
  l_mname="cramfs" # set module name
  l_mtype="fs" # set module type
  l_searchloc="/lib/modprobe.d/*.conf /usr/local/lib/modprobe.d/*.conf /run/modprobe.d/*.conf
/etc/modprobe.d/*.conf"
  l_mpath="/lib/modules/**/kernel/$l_mtype"
  l_mpname="$(tr '-' '_' <<< "$l_mname")"
  l_mndir="$(tr '-' '/' <<< "$l_mname")"
  module_loadable_chk()
  {
   # Check if the module is currently loadable
   l_loadable="$(modprobe -n -v "$l_mname")"
   [ "$(wc -l <<< "$l_loadable")" -gt "1" ] && l_loadable="$(grep -P -"(^\h*install|\b$l_mname)\b" <<< "$l_loadable")"
   if grep -Pq -- '^\h*install \/bin\/(true|false)' <<< "$l_loadable"; then
     l_output="$l_output\n - module: \"$l_mname\" is not loadable: \"$l_loadable\""
   else
     l_output2="$l_output2\n - module: \"$l_mname\" is loadable: \"$l_loadable\""
   fi
  }
  module_loaded_chk()
  {
   # Check if the module is currently loaded
   if ! lsmod | grep "$l_mname" > /dev/null 2>&1; then
     l_output="$l_output\n - module: \"$l_mname\" is not loaded"
   else
     l_output2="$l_output2\n - module: \"$l_mname\" is loaded"
   fi
  }
  module_deny_chk()
  {
   # Check if the module is deny listed
   l_dl="y"
   if modprobe --showconfig | grep -Pq -- '^\h*blacklist\h+'"$l_mpname"'\b'; then
     l_output="$l_output\n - module: \"$l_mname\" is deny listed in: \"$(grep -Pls -"^\h*blacklist\h+$l_mname\b" $l_searchloc)\""
   else
     l_output2="$l_output2\n - module: \"$l_mname\" is not deny listed"
   fi
  }
  # Check if the module exists on the system
  for l_mdir in $l_mpath; do
   if [ -d "$l_mdir/$l_mndir" ] && [ -n "$(ls -A $l_mdir/$l_mndir)" ]; then
     l_output3="$l_output3\n - \"$l_mdir\""
     [ "$l_dl" != "y" ] && module_deny_chk
     if [ "$l_mdir" = "/lib/modules/$(uname -r)/kernel/$l_mtype" ]; then
      module_loadable_chk
      module_loaded_chk
     fi
   else
     l_output="$l_output\n - module: \"$l_mname\" doesn't exist in \"$l_mdir\""
   fi
  done
  # Report results. If no failures output in l_output2, we pass
  [ -n "$l_output3" ] && echo -e "\n\n -- INFO --\n - module: \"$l_mname\" exists in:$l_output3"
  if [ -z "$l_output2" ]; then
   echo -e "\n- Audit Result:\n ** PASS **\n$l_output\n"
  else
   echo -e "\n- Audit Result:\n ** FAIL **\n - Reason(s) for audit failure:\n$l_output2\n"
   [ -n "$l_output" ] && echo -e "\n- Correctly set:\n$l_output\n"
  fi
}

#### Page 22

```

-----

### Remediation:

 Run the following script to disable the cramfs module: -IF- the module is available in the running kernel:

#### • Create a file ending in .conf with install cramfs /bin/false in the
```
    /etc/modprobe.d/ directory

 • Create a file ending in .conf with blacklist cramfs in the /etc/modprobe.d/
### directory

#### • Unload cramfs from the kernel

### -IF- available in ANY installed kernel:

#### • Create a file ending in .conf with blacklist cramfs in the /etc/modprobe.d/
### directory

 -IF- the kernel module is not available on the system or pre-compiled into the kernel:

#### • No remediation is necessary

 Page 23

```

-----

```
#!/usr/bin/env bash
{
  l_mname="cramfs" # set module name
  l_mtype="fs" # set module type
  l_mpath="/lib/modules/**/kernel/$l_mtype"
  l_mpname="$(tr '-' '_' <<< "$l_mname")"
  l_mndir="$(tr '-' '/' <<< "$l_mname")"
  module_loadable_fix()
  {
   # If the module is currently loadable, add "install {MODULE_NAME} /bin/false" to a file in
"/etc/modprobe.d"
   l_loadable="$(modprobe -n -v "$l_mname")"
   [ "$(wc -l <<< "$l_loadable")" -gt "1" ] && l_loadable="$(grep -P -"(^\h*install|\b$l_mname)\b" <<< "$l_loadable")"
   if ! grep -Pq -- '^\h*install \/bin\/(true|false)' <<< "$l_loadable"; then
     echo -e "\n - setting module: \"$l_mname\" to be not loadable"
     echo -e "install $l_mname /bin/false" >> /etc/modprobe.d/"$l_mpname".conf
   fi
  }
  module_loaded_fix()
  {
   # If the module is currently loaded, unload the module
   if lsmod | grep "$l_mname" > /dev/null 2>&1; then
     echo -e "\n - unloading module \"$l_mname\""
     modprobe -r "$l_mname"
   fi
  }
  module_deny_fix()
  {
   # If the module isn't deny listed, denylist the module
   if ! modprobe --showconfig | grep -Pq -- "^\h*blacklist\h+$l_mpname\b"; then
     echo -e "\n - deny listing \"$l_mname\""
     echo -e "blacklist $l_mname" >> /etc/modprobe.d/"$l_mpname".conf
   fi
  }
  # Check if the module exists on the system
  for l_mdir in $l_mpath; do
   if [ -d "$l_mdir/$l_mndir" ] && [ -n "$(ls -A $l_mdir/$l_mndir)" ]; then
     echo -e "\n - module: \"$l_mname\" exists in \"$l_mdir\"\n - checking if disabled..."
     module_deny_fix
     if [ "$l_mdir" = "/lib/modules/$(uname -r)/kernel/$l_mtype" ]; then
      module_loadable_fix
      module_loaded_fix
     fi
   else
     echo -e "\n - module: \"$l_mname\" doesn't exist in \"$l_mdir\"\n"
   fi
  done
  echo -e "\n - remediation of module: \"$l_mname\" complete\n"
}

### References:

 1. NIST SP 800-53 Rev. 5: CM-7

#### Page 24

```

-----

### CIS Controls:

 Controls
 Control IG 1 IG 2 IG 3 Version

 4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software
 v8 Uninstall or disable unnecessary services on enterprise assets and software, ● ●

##### such as an unused file sharing service, web application module, or service function.

### 9.2 Ensure Only Approved Ports, Protocols and Services
 v7 Are Running ● ●

##### Ensure that only network ports, protocols, and services listening on a system
 with validated business needs, are running on each system.

### MITRE ATT&CK Mappings:

 Techniques / Sub Tactics Mitigations techniques

 T1005, T1005.000 TA0005 M1050

#### Page 25

|Controls Version|Control|IG 1|IG 2|IG 3|
|---|---|---|---|---|
|v8|4.8 Uninstall or Disable Unnecessary Services on Enterprise Assets and Software Uninstall or disable unnecessary services on enterprise assets and software, such as an unused file sharing service, web application module, or service function.||●|●|
|v7|9.2 Ensure Only Approved Ports, Protocols and Services Are Running Ensure that only network ports, protocols, and services listening on a system with validated business needs, are running on each system.||●|●|

|MITRE ATT&CK Mappings:|Col2|Col3|
|---|---|---|
|Techniques / Sub- techniques|Tactics|Mitigations|
|T1005, T1005.000|TA0005|M1050|


-----

