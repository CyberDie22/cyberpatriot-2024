# (L1) Ensure 'Disable Update' is set to 'Disabled'

## Description

This policy setting configures if the Firefox browser can receive updates. The recommended state for this setting is: Disabled.

Disabling updates for Firefox creates a significant security risk in an enterprise environment. When updates are disabled, vulnerabilities discovered in Firefox after installation are not addressed, increasing the attack surface of affected systems.

Impact of leaving updates disabled:

- Increased vulnerability to known and unknown exploits
- Lack of protection against newly discovered vulnerabilities
- Maintenance issues and potential incompatibilities
- Decreased overall security posture for the enterprise

It's crucial to note that this is not describing a vulnerability in Firefox itself, but rather a policy that actively creates vulnerabilities by preventing appropriate updates.

## Audit

### Windows

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```
3. Verify that the "Disable Update" setting is set to "Disabled"

Alternatively, check the following registry location:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox:DisableAppUpdate
```

Confirm that the REG_DWORD value is set to 0.

### Linux

Firefox policies on Linux are typically managed through a JSON file. To audit the update settings:

1. Check for the existence of a policy file, usually located at:
   ```
   /etc/firefox/policies/policies.json
   ```
2. If the file exists, verify that it does not contain a "DisableAppUpdate" entry, or that the entry is set to false.

## Remediation

### Windows

1. Open the Group Policy Management Console
2. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox
   ```
3. Set the "Disable Update" policy to "Disabled"

Note: If the Firefox administrative template is not present, you may need to download and install it from the [Mozilla Policy Templates GitHub repository](https://github.com/mozilla/policy-templates/releases).

### Linux

1. If a policy file doesn't exist, no action is needed as updates should be enabled by default.
2. If a policy file exists at `/etc/firefox/policies/policies.json`, ensure it does not contain a "DisableAppUpdate" entry, or set it to false:

   ```json
   {
     "policies": {
       "DisableAppUpdate": false
     }
   }
   ```

3. Save the file and restart Firefox for the changes to take effect.

For both Windows and Linux, ensure that your software management processes allow for timely application of Firefox updates to maintain system security.