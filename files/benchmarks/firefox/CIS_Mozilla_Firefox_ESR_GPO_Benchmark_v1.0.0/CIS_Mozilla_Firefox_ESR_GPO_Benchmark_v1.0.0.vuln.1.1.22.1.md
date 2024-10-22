# (L1) Ensure 'Cryptomining' is set to 'Enabled'

## Description

Mozilla Firefox includes a built-in Cryptomining Protection feature that automatically blocks known crypto mining domains that distribute crypto mining scripts. However, if this feature is not properly configured through Group Policy, it can lead to a vulnerability where malicious cryptomining scripts could potentially load and execute on user machines without detection.

**Vulnerability:** Incorrect or Missing Group Policy Configuration for Cryptomining Protection

This vulnerability arises from the lack of proper configuration at the enterprise level through Group Policy. The impact of this vulnerability includes:

- Unauthorized access to a user's CPU resources for cryptocurrency mining
- Performance degradation in affected devices
- Potential disruption of legitimate operations

The severity of this vulnerability ranges from Medium to High, depending on the organization's security posture and the sensitivity of the impacted systems.

## Audit

To audit this setting, follow these steps:

1. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Tracking Protection\Cryptomining
   ```
2. Confirm that it is set to "Enabled".

Additionally, you can check the following registry location:

```
HKLM\SOFTWARE\Policies\Mozilla\Firefox\EnableTrackingProtection:Cryptomining
```

Ensure it has a REG_DWORD value of 1.

## Remediation

### Windows

To establish the recommended configuration via Group Policy:

1. Download the additional Group Policy template (firefox.admx/adml) from [this link](https://github.com/mozilla/policy-templates/releases).
2. Install the template in your Group Policy management environment.
3. Navigate to the following UI path:
   ```
   Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox\Tracking Protection\Cryptomining
   ```
4. Set the policy to "Enabled".

### Linux

For Linux systems, Firefox configurations are typically managed through a `policies.json` file. To enable Cryptomining Protection:

1. Locate or create the `policies.json` file in the Firefox installation directory (usually `/etc/firefox/policies/`).
2. Add or modify the following configuration:
   ```json
   {
     "policies": {
       "EnableTrackingProtection": {
         "Cryptomining": true
       }
     }
   }
   ```
3. Save the file and restart Firefox for the changes to take effect.

Note: Ensure you have the necessary permissions to modify system-wide Firefox configurations.

For both Windows and Linux environments, it's recommended to:

1. Regularly update Firefox to the latest version.
2. Implement a comprehensive security awareness program to educate users about the risks of cryptomining.
3. Consider deploying additional security tools, such as endpoint detection and response solutions, for layered protection.