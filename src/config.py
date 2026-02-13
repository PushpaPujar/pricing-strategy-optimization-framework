"""
Configuration settings for the pricing optimization framework.
"""

# Margin Thresholds
MIN_ACCEPTABLE_MARGIN = 20.0  # Minimum acceptable margin percentage
TARGET_GROSS_MARGIN = 35.0    # Target gross margin percentage
CRITICAL_MARGIN_THRESHOLD = 15.0  # Below this is CRITICAL

# Price Adjustment Factors
MAX_PRICE_INCREASE = 0.30  # Maximum 30% price increase
MAX_PRICE_DECREASE = 0.10  # Maximum 10% price decrease
PRICE_ADJUSTMENT_STEP = 0.50  # Price adjustment in $0.50 increments

# Inventory Pressure Weights
INVENTORY_WEIGHT_HEALTHY = 1.0
INVENTORY_WEIGHT_MODERATE = 1.2
INVENTORY_WEIGHT_ELEVATED = 1.5

# Velocity Categories
VELOCITY_THRESHOLD_SLOW = 5  # < 5 units/day
VELOCITY_THRESHOLD_AVERAGE = 10  # 5-10 units/day
VELOCITY_THRESHOLD_FAST = 10  # > 10 units/day

# Recommendation Urgency
URGENCY_CRITICAL = "URGENT: Below Min Margin"
URGENCY_HIGH = "HIGH: Adjust for Optimization"
URGENCY_MEDIUM = "MEDIUM: Consider Adjustment"
URGENCY_LOW = "LOW: Maintain Price"

# Analysis Settings
COMPETITOR_PRICE_WEIGHT = 0.40
COST_WEIGHT = 0.30
INVENTORY_WEIGHT = 0.20
VELOCITY_WEIGHT = 0.10

# Data Validation
REQUIRED_COLUMNS = [
    'SKU', 'Product_description', 'Cost', 'Current_Price',
    'Minimum_Acceptable_Margin_%', 'Target_Gross_Margin_%'
]
