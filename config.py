# Safe version: no hardcoded secret is stored in the source code.
# The value should come from an environment variable or GitHub Secret.

import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")

# NOVA-KEY-123456
# NOVA-KEY-789012
# NOVA-KEY-456789
# NOVA-KEY-12345
# NOVA-KEY-1234567
# OTHER-KEY-123456
