# (L1) Ensure 'Application Autoupdate' is set to 'Enabled'

## Description

This policy setting configures whether Firefox automatically downloads and installs updates as they are made available. The recommended state for this setting is: Enabled.

The vulnerability arises from a lack of automated updates for Mozilla Firefox. A system with this setting disabled is at risk of running outdated versions of the browser. Outdated versions are far more likely to include known security vulnerabilities, exposing the machine to malware and unauthorized access.

This isn't a vulnerability in Firefox itself, but a configuration issue that impedes the application from receiving and applying security updates. This leaves the system actively exposed to any security risk inherent to those older Firefox versions, which may include vulnerabilities for malicious code execution, information disclosure, or other attack vectors.

**Impact:**
Without automatic updates, any security vulnerability discovered and patched for later versions of Firefox won't be applied to the system. This introduces a significant escalation of vulnerability risk to the entire environment. An attacker could exploit these outdated versions to gain unauthorized access, compromise data, or execute arbitrary code.

## Audit

### Windows

1. Open the Group Policy Management Editor.
2. Navigate to the following UI path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox`
3. Locate the "Application Autoupdate" setting.
4. Verify that it is set to "Enabled".

Alternatively, you can check the registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Verify that the `AppAutoUpdate` value exists and is set to `1` (REG_DWORD).

### Linux

Firefox on Linux typically doesn't use Group Policy. However, you can check the current update settings:

1. Open Firefox.
2. In the address bar, type `about:preferences#general`.
3. Scroll down to the "Firefox Updates" section.
4. Verify that "Automatically install updates" is checked.

## Remediation

### Windows

To establish the recommended configuration via Group Policy:

1. Ensure you have the necessary Group Policy template (firefox.admx/adml). If not, download it from: https://github.com/mozilla/policy-templates/releases
2. Open the Group Policy Management Editor.
3. Navigate to the following UI path:
   `Computer Configuration\Policies\Administrative Templates\Mozilla\Firefox`
4. Locate the "Application Autoupdate" setting.
5. Set it to "Enabled".

If you need to set this via registry:

1. Open the Registry Editor.
2. Navigate to the following key:
   `HKLM\SOFTWARE\Policies\Mozilla\Firefox`
3. Create a new DWORD value named `AppAutoUpdate` if it doesn't exist.
4. Set the value to `1`.

### Linux

On Linux systems, you typically manage Firefox settings through configuration files:

1. Create or edit the file `/etc/firefox/policies/policies.json`.
2. Add the following content:

```json
{
  "policies": {
    "AppAutoUpdate": true
  }
}
```

3. Save the file and restart Firefox.

Note: The exact location of the policies file may vary depending on your Linux distribution. Some systems might use `/usr/lib/firefox/distribution/policies.json` instead.