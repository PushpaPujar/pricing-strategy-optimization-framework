"""
Unit tests for the pricing analyzer module.
"""

import pytest
import pandas as pd
from src.pricing_analyzer import PricingAnalyzer


class TestPricingAnalyzer:
    """Test cases for PricingAnalyzer class."""
    
    @pytest.fixture
    def sample_data(self):
        """Create sample pricing data for testing."""
        return pd.DataFrame({
            'SKU': ['MN-01', 'MN-02'],
            'Product_description': ['Product 1', 'Product 2'],
            'Current_Price': [38.9, 33.9],
            'Cost': [16.0, 12.0],
            'Current_Margin_%': [16.97, 21.53],
            'Margin_Health': ['CRITICAL', 'OPPORTUNITY'],
            'Recommended_Price': [40.9, 33.9],
            'Price_Change_%': [5.14, 0.0],
            'Recommendation_Action': ['URGENT: Below Min Margin', 'Maintain Price']
        })
    
    def test_analyzer_initialization(self):
        """Test analyzer can be initialized."""
        analyzer = PricingAnalyzer()
        assert analyzer.data is None
    
    def test_load_data(self, sample_data, tmp_path):
        """Test data loading."""
        csv_file = tmp_path / "test_data.csv"
        sample_data.to_csv(csv_file, index=False)
        
        analyzer = PricingAnalyzer(str(csv_file))
        assert analyzer.data is not None
        assert len(analyzer.data) == 2
    
    def test_analyze_margins(self, sample_data, tmp_path):
        """Test margin analysis."""
        csv_file = tmp_path / "test_data.csv"
        sample_data.to_csv(csv_file, index=False)
        
        analyzer = PricingAnalyzer(str(csv_file))
        margins = analyzer.analyze_margins()
        
        assert 'SKU' in margins.columns
        assert 'Current_Margin_%' in margins.columns
        assert len(margins) == 2


if __name__ == "__main__":
    pytest.main([__file__])
