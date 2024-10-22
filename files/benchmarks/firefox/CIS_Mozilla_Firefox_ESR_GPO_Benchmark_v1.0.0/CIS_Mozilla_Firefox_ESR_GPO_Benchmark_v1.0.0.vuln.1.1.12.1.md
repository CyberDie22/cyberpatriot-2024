# (L1) Ensure 'Activate Flash on websites' is set to 'Disabled'

## Description

This vulnerability involves the risk of exploiting unpatched vulnerabilities in the Adobe Flash Player plugin for Mozilla Firefox. Mozilla Firefox no longer supports Adobe Flash, having ended support in late 2020. This means that any Flash-based content a user might encounter is running unsupported software.

Key points:

- **Vulnerability Type:** Exposure to unpatched vulnerabilities
- **Affected Software:** Adobe Flash Player plugin (for Firefox)
- **Exploitation Vector:** An attacker could exploit vulnerabilities in the Flash plugin, potentially leading to Remote Code Execution (RCE)
- **Impact:** Risk of malicious code execution and potential system compromise
- **Mitigation:** Disable the Flash plugin in Firefox using the described Group Policy setting

The vulnerability is addressed by removing the possibility of outdated Flash being used on the system. Configuring the "Activate Flash on websites" setting to "Disabled" is the remediation and is mirrored in the registry.

## Audit

To audit this setting:

1. Open the Group Policy Management Console
2. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Flash
3. Verify that 'Activate Flash on websites' is set to 'Disabled'

Alternatively, check the following registry location:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox\FlashPlugin
```

Confirm that the 'Default' value (REG_DWORD) is set to 0.

## Remediation

### Windows

1. Download the Firefox Group Policy template (firefox.admx/adml) from: https://github.com/mozilla/policy-templates/releases
2. Copy the template files to your Policy Definitions folder (usually %SystemRoot%\PolicyDefinitions)
3. Open the Group Policy Management Console
4. Navigate to Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Flash
5. Set 'Activate Flash on websites' to 'Disabled'
6. Run 'gpupdate /force' to apply the changes

### Linux

Firefox on Linux typically doesn't use Group Policy. Instead, you can disable Flash for all users by creating or editing the global Firefox configuration file:

1. Open a terminal
2. Create or edit the file `/etc/firefox/policies/policies.json`
3. Add the following content:

```json
{
  "policies": {
    "FlashPlugin": {
      "Default": false
    }
  }
}
```

4. Save the file and restart Firefox for the changes to take effect

Note: Ensure that no Flash plugins are installed on the system to further prevent its use.