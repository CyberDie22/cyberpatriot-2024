# (L1) Ensure 'Password Manager' is set to 'Disabled'

## Description

The Firefox Password Manager feature, when enabled, allows users to save their passwords within the browser. While this can be convenient, it poses a significant security risk if an attacker gains access to the user's system. This vulnerability arises from the potential unauthorized access to stored passwords, especially in cases of unattended or unlocked workstations.

**Impact:**
- Increased risk of data breaches if an attacker gains system access
- Potential compromise of multiple user accounts if passwords are extracted
- Elevated risk for systems with weak access controls or frequently left unattended

**Affected Systems:** Windows systems using Mozilla Firefox and managed by Group Policy

**CIS Controls References:** 
- 4.8: Uninstall or Disable Unnecessary Services on Enterprise Assets and Software
- 9.2: Use DNS Filtering Services

## Audit

To audit this setting:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Password Manager
3. Verify that the "Password Manager" setting is set to "Disabled"

Alternatively, check the following registry location:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox:PasswordManagerEnabled
```

The REG_DWORD value should be set to 0.

## Remediation

### Windows

1. Ensure you have the necessary Firefox Group Policy template (firefox.admx/adml) installed. If not, download it from the official Mozilla website.
2. Open the Group Policy Management Console
3. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox
4. Locate and double-click on "Password Manager"
5. Select "Disabled"
6. Click "Apply" and then "OK"
7. Run `gpupdate /force` from a command prompt to apply the changes immediately

### Linux

For Linux systems, Firefox typically doesn't use Group Policy. However, you can disable the password manager through the following steps:

1. Open Firefox
2. Navigate to "about:config" in the address bar
3. Search for "signon.rememberSignons"
4. Set its value to "false"

For system-wide configuration on Linux:

1. Create or edit the file `/etc/firefox/policies/policies.json`
2. Add the following content:

```json
{
  "policies": {
    "PasswordManagerEnabled": false
  }
}
```

3. Save the file and restart Firefox

Note: Ensure proper file permissions are set to prevent unauthorized modifications.