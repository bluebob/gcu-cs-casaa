Create a validation script benchmark-suite/validate_suite.py that 
checks each test case in the Claude benchmark suite before running 
the full evaluation. 

For each test case in each language CSV (python, go, java, javascript):

1. Verify the Dockerfile exists at the path in test_case_path
2. Verify the CVE ID exists in NIST NVD API:
   https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_id}
3. Language-specific dependency checks:
   - Go: verify go.mod exists; check each module@version resolves 
     via https://proxy.golang.org/{module}/@v/{version}.info
   - Python: verify requirements.txt exists; check each package==version 
     exists via https://pypi.org/pypi/{package}/{version}/json
   - Java: verify pom.xml exists; check each dependency exists on 
     Maven Central via https://search.maven.org/solrsearch/select
   - JavaScript: verify package.json exists; check each dependency 
     version exists via https://registry.npmjs.org/{package}/{version}

4. Output a clear pass/fail report per test case showing which 
   checks failed and why

5. Exit with code 1 if any test cases fail validation

Use uv for dependency management. The script should run from the 
benchmark-suite directory.

Known failure to validate against: claude/go/CVE-2022-29153 has 
github.com/hashicorp/consul/api@v1.11.3 which is an invalid module 
revision and should be reported as a failure.
