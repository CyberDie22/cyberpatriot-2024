# (L1) Ensure 'Disable Developer Tools' is set to 'Enabled'

## Description

This setting configures whether development tools are available to the user in Firefox. Firefox Developer Tools is a set of web developer tools built into Firefox that can be used to examine, edit, and debug HTML, CSS, and JavaScript.

When Developer Tools are enabled in a production environment, it can lead to potential information disclosure risks. An attacker could potentially gather sensitive information about the browser environment, including:

- Firefox version
- Installed extensions and plugins
- Application code details
- Backend system information
- Operating system details
- Browser configuration settings

This information could be used by attackers to identify vulnerabilities and plan further attacks. The recommended state for this setting is: Enabled (which disables the Developer Tools).

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Developer Tools
   ```
3. Verify that the setting is set to "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor
2. Navigate to the following key:
   ```
   HKLM\SOFTWARE\Policies\Mozilla\Firefox
   ```
3. Verify that the "DisableDeveloperTools" value exists and is set to 1 (DWORD)

### Linux:

Firefox policies on Linux are typically managed through a JSON file. To audit:

1. Check for the existence of the policy file:
   ```
   /etc/firefox/policies/policies.json
   ```
2. Verify that the file contains the following configuration:
   ```json
   {
     "policies": {
       "DisableDeveloperTools": true
     }
   }
   ```

## Remediation

To remediate this issue:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Disable Developer Tools
   ```
3. Set the policy to "Enabled"

If the Firefox Administrative Templates are not available:

1. Download the policy templates from: https://github.com/mozilla/policy-templates/releases
2. Extract and copy the `firefox.admx` file to `%SystemRoot%\PolicyDefinitions\`
3. Copy the `firefox.adml` file to `%SystemRoot%\PolicyDefinitions\en-US\`

### Linux:

1. Create or edit the file `/etc/firefox/policies/policies.json`
2. Ensure it contains the following content:
   ```json
   {
     "policies": {
       "DisableDeveloperTools": true
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect

Note: Ensure that users who require Developer Tools for legitimate purposes are given the necessary permissions through appropriate user roles or separate browser instances.