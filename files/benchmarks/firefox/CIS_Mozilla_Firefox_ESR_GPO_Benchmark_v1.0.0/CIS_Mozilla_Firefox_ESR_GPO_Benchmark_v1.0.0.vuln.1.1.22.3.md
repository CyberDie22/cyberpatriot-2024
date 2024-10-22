# (L1) Ensure 'Email Tracking' is set to 'Enabled'

## Description

This policy setting configures Firefox's Enhanced Tracking Protection feature, specifically focusing on email tracking. When enabled, Firefox will automatically block known third-party tracking cookies related to email tracking. This setting is recommended for both server and workstation environments to enhance user privacy and reduce potential attack vectors.

Enabling this setting is a security best practice that aims to prevent websites from tracking user activity across different sites, potentially enhancing user privacy. However, it's important to note that this is a configuration setting rather than a traditional security vulnerability.

## Audit

To audit this setting:

### Windows:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Tracking Protection > Email Tracking
3. Verify that the setting is set to "Enabled"

Alternatively, you can check the registry:

1. Open the Registry Editor (regedit.exe)
2. Navigate to: `HKLM\SOFTWARE\Policies\Mozilla\Firefox\EnableTrackingProtection`
3. Verify that the `EmailTracking` value is set to `1` (REG_DWORD)

### Linux:

Firefox policies on Linux are typically managed through a JSON configuration file. To audit:

1. Locate the policy file (usually in `/etc/firefox/policies/` or `/usr/lib/firefox/distribution/`)
2. Open the `policies.json` file
3. Look for a section similar to:
   ```json
   {
     "policies": {
       "EnableTrackingProtection": {
         "EmailTracking": true
       }
     }
   }
   ```
4. Verify that `EmailTracking` is set to `true`

## Remediation

To implement the recommended configuration:

### Windows:

Using Group Policy:

1. Open the Group Policy Management Console
2. Navigate to: Computer Configuration > Policies > Administrative Templates > Mozilla > Firefox > Tracking Protection > Email Tracking
3. Set the policy to "Enabled"

If using registry:

1. Open the Registry Editor (regedit.exe)
2. Navigate to: `HKLM\SOFTWARE\Policies\Mozilla\Firefox\EnableTrackingProtection`
3. Create a DWORD value named `EmailTracking` if it doesn't exist
4. Set the value to `1`

### Linux:

1. Locate or create the policy file (typically in `/etc/firefox/policies/` or `/usr/lib/firefox/distribution/`)
2. Edit or create `policies.json`
3. Ensure it contains:
   ```json
   {
     "policies": {
       "EnableTrackingProtection": {
         "EmailTracking": true
       }
     }
   }
   ```
4. Save the file and restart Firefox for changes to take effect

After implementing these changes, Firefox will block known third-party tracking cookies related to email tracking, enhancing user privacy across both server and workstation environments.