# (L1) Ensure 'Disable Firefox Studies' is set to 'Enabled'

## Description

Firefox Studies, also known as Shield Studies, are controlled tests conducted by Mozilla to evaluate proposed changes to Firefox before releasing them to the general user base. These studies collect data on Firefox usage for research and development purposes. However, this data collection can potentially lead to the inadvertent sharing of sensitive user information.

The vulnerability lies in the configuration of the "Disable Firefox Studies" setting. When this setting is not enabled, Firefox may collect and transmit the following types of data:

- Usage hours
- Days Firefox was used
- Study name and ID
- Experimental branch
- Study status transitions

While this data collection is not inherently malicious, it poses a risk of sensitive user or company data being disclosed to Mozilla without explicit consent.

It's important to note that this is not a software flaw, but rather a configuration issue that, if left unaddressed, could lead to unintended data sharing.

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Editor.
2. Navigate to the following path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox`
3. Look for the "Disable Firefox Studies" policy.
4. Verify that it is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Check for a REG_DWORD value named `DisableFirefoxStudies`.
4. Verify that its value is set to 1.

### Linux:

Firefox policies on Linux are typically managed through a JSON file. To audit:

1. Check for the existence of the policy file:
   `/etc/firefox/policies/policies.json`
2. If the file exists, open it and look for the following configuration:
   ```json
   {
     "policies": {
       "DisableFirefoxStudies": true
     }
   }
   ```

## Remediation

To remediate this vulnerability:

### Windows:

1. Ensure you have the necessary ADMX/ADML template files for Firefox Group Policy. These can be downloaded from Mozilla's official website.
2. Open the Group Policy Editor.
3. Navigate to:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox`
4. Find and double-click on "Disable Firefox Studies".
5. Set it to "Enabled".
6. Click "Apply" and then "OK".

If you prefer to use the registry:

1. Open the Registry Editor.
2. Navigate to:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Create a new REG_DWORD value named `DisableFirefoxStudies` if it doesn't exist.
4. Set its value to 1.

### Linux:

1. Create or edit the file `/etc/firefox/policies/policies.json`.
2. Ensure it contains the following content:
   ```json
   {
     "policies": {
       "DisableFirefoxStudies": true
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

After applying these changes, Firefox Studies will be disabled, preventing the collection and transmission of potentially sensitive user data.