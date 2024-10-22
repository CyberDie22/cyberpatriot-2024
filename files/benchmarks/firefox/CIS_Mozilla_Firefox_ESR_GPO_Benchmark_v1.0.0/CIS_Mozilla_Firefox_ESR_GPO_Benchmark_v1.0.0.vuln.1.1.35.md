# (L1) Ensure 'Disable Telemetry' is set to 'Enabled'

## Description

Firefox by default sends information about Firefox to Mozilla servers. This data can include, but is not limited to IP address, system specifications, browsing history, bookmarks, and open tabs. The recommended state for this setting is: Enabled.

Sending data to Firefox could lead to sensitive data being exposed. This configuration issue relates to the Group Policy "Disable Telemetry" being incorrectly set to "Disabled" within Windows' Group Policy Management. While not a direct security vulnerability, it does reduce the effectiveness of the software and impedes the development and refinement process.

**Affected Software:** Mozilla Firefox (browser)
**Affected Systems:** Windows systems configured with the described Group Policy
**Severity:** Low

## Audit

To audit this setting:

1. Open the Group Policy Management Console (gpmc.msc)
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Telemetry
   ```
3. Verify that the setting is set to "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe)
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the "DisableTelemetry" value exists and is set to 1 (DWORD)

## Remediation

### Windows:

1. Download and install the additional Group Policy template (firefox.admx/adml) from [Mozilla's policy templates repository](https://github.com/mozilla/policy-templates/releases)
2. Open the Group Policy Management Console (gpmc.msc)
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Telemetry
   ```
4. Set the policy to "Enabled"
5. Run `gpupdate /force` from an elevated command prompt to apply the changes

### Linux:

Firefox on Linux typically doesn't use Group Policies. Instead, you can disable telemetry by:

1. Open Firefox
2. Type `about:config` in the address bar and press Enter
3. Accept the risk warning
4. Search for `datareporting.healthreport.uploadEnabled`
5. Set it to `false` by double-clicking on it
6. Search for `datareporting.policy.dataSubmissionEnabled`
7. Set it to `false` by double-clicking on it

Alternatively, you can create or edit the `policies.json` file:

1. Locate or create the following directory:
   ```
   /usr/lib/firefox/distribution/
   ```
2. Create or edit the `policies.json` file in this directory
3. Add the following content:
   ```json
   {
     "policies": {
       "DisableTelemetry": true
     }
   }
   ```
4. Save the file and restart Firefox