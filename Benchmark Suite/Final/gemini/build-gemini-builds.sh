#!/usr/bin/env bash
# validate_builds.sh
# Attempts docker build for each test case Dockerfile and reports pass/fail
# Run from benchmark-suite root

set -uo pipefail

SUITE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RESULTS_DIR="$SUITE_DIR/gemini-results"

# Create or clean the results directory
if [ -d "$RESULTS_DIR" ]; then
    # Remove contents of the directory
    find "$RESULTS_DIR" -mindepth 1 -delete
else
    # Create the directory
    mkdir -p "$RESULTS_DIR"
fi

PASS=0
FAIL=0
FAILURES=()

EXCLUDED_LANGUAGES=("cpp")


for csv in "$SUITE_DIR"/gemini/*/*-set.csv; do
    # lang_dir="$(dirname "$csv")"
    while IFS=, read -r cve_id cvss affected_lib affected_ver test_case_path base_image; do
        lang=$(basename "$(dirname "$csv")")
        if [[ " ${EXCLUDED_LANGUAGES[*]} " =~ " ${lang} " ]]; then
            echo "Skipping excluded language: $lang"
            continue
        fi
        [[ "$cve_id" =~ ^#.*$ ]] && continue
        [[ "$cve_id" == "cve_id" ]] && continue
        dockerfile="$SUITE_DIR/$test_case_path/Dockerfile"
        [[ ! -f "$dockerfile" ]] && continue
        printf "Building %s... " "$cve_id"
        if docker build --platform linux/amd64 -t "test-$(echo "$cve_id" | tr '[:upper:]' '[:lower:]')" "$(dirname "$dockerfile")" > "$RESULTS_DIR/$cve_id.txt" 2>&1; then
            echo "pass"
            ((PASS++))
            rm "$RESULTS_DIR/$cve_id.txt"
        else
            echo "FAIL"
            ((FAIL++))
            FAILURES+=("$cve_id")
        fi
    done < "$csv"
done

echo ""
echo "Results: $PASS passed, $FAIL failed"
for f in "${FAILURES[@]}"; do
    echo "  FAIL: $f"
done

exit 0
