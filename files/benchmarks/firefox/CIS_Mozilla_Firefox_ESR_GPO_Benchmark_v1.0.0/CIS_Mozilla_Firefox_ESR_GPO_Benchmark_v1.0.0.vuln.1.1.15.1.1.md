# (L1) Ensure 'Block new requests asking to access location' is set to 'Enabled'

## Description

This policy setting determines whether Firefox will provide geographic location information to websites. The recommended state for this setting is: Enabled.

Geo-location services can expose private information to remote websites. By enabling this policy, new requests from websites to access the user's location will be blocked, enhancing privacy and security.

However, it's important to note that this is a misconfiguration rather than a traditional vulnerability. While it protects user privacy, it may impact the functionality of websites that rely on location data, such as mapping services.

## Audit

To audit this setting:

### Windows:
1. Open the Group Policy Management Console (GPMC).
2. Navigate to the following UI path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Permissions\Location\Block new requests asking to access location`
3. Verify that the setting is set to "Enabled".

Alternatively, you can check the registry:
1. Open the Registry Editor.
2. Navigate to the following location:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox\Permissions\Location`
3. Verify that the `BlockNewRequests` value is set to `1` (REG_DWORD).

### Linux:
Firefox policies on Linux are typically managed through a JSON file. To audit:

1. Check for the presence of a `policies.json` file in one of these locations:
   - `/etc/firefox/policies/`
   - `/usr/lib/firefox/distribution/`
2. Open the file and look for a section similar to:
   ```json
   {
     "policies": {
       "Permissions": {
         "Location": {
           "BlockNewRequests": true
         }
       }
     }
   }
   ```
3. Verify that `BlockNewRequests` is set to `true`.

## Remediation

To implement the recommended configuration:

### Windows:
1. Open the Group Policy Management Console (GPMC).
2. Navigate to: `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Permissions\Location\Block new requests asking to access location`
3. Set the policy to "Enabled".

Note: If the policy path doesn't exist, you need to download and install the Firefox ADMX template from: https://github.com/mozilla/policy-templates/releases

### Linux:
1. Create or edit the `policies.json` file in one of these locations:
   - `/etc/firefox/policies/`
   - `/usr/lib/firefox/distribution/`
2. Add or modify the following configuration:
   ```json
   {
     "policies": {
       "Permissions": {
         "Location": {
           "BlockNewRequests": true
         }
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Remember to consider the impact on user experience and functionality when implementing this policy. You may want to create exceptions for trusted websites or implement a more granular approach to location sharing.