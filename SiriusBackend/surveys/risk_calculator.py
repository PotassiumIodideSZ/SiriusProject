"""
Risk Calculator Module

This module provides formula-based risk score calculation from questionnaire answers.
This is a placeholder implementation that will be replaced with AI-based calculation
in the future. The current implementation uses a weighted formula approach.

TODO: Replace with AI service integration when available.
"""

from typing import List, Dict, Any


def calculate_risk_score(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Calculate risk score from questionnaire answers.
    
    This is a placeholder implementation using a weighted formula.
    In the future, this will be replaced with AI-based analysis.
    
    Args:
        answers: List of dictionaries containing question_id and answer_value
                 Example: [{'question_id': 1, 'answer_value': 5}, ...]
    
    Returns:
        Dictionary containing:
        - risk_score: Integer from 0-100
        - risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
        - asset_allocation: Dict with percentage allocations
        - recommendations: List of recommendation strings
        - key_traits: List of trait strings
    
    Question Groups:
    - Logic & Reasoning (Questions 1-7): Higher scores = more analytical approach
    - Emotional Control (Questions 8-12): Higher scores = better emotional stability
    - Independence (Questions 13-17): Higher scores = more independent decision-making
    - Willpower & Leadership (Questions 18-23): Higher scores = stronger character
    """
    
    # Initialize scores for each category
    logic_score = 0
    emotional_score = 0
    independence_score = 0
    willpower_score = 0
    
    # Count answers in each category
    logic_count = 0
    emotional_count = 0
    independence_count = 0
    willpower_count = 0
    
    # Process each answer
    for answer in answers:
        question_id = answer.get('question_id')
        answer_value = answer.get('answer_value', 3)  # Default to neutral
        
        # Normalize answer value (1-5) to score (0-100)
        # 1 = Fully agree (low risk) -> 0
        # 5 = Fully disagree (high risk) -> 100
        normalized_score = ((answer_value - 1) / 4) * 100
        
        # Categorize by question ID
        if 1 <= question_id <= 7:
            logic_score += normalized_score
            logic_count += 1
        elif 8 <= question_id <= 12:
            emotional_score += normalized_score
            emotional_count += 1
        elif 13 <= question_id <= 17:
            independence_score += normalized_score
            independence_count += 1
        elif 18 <= question_id <= 23:
            willpower_score += normalized_score
            willpower_count += 1
    
    # Calculate average scores for each category
    logic_avg = logic_score / logic_count if logic_count > 0 else 50
    emotional_avg = emotional_score / emotional_count if emotional_count > 0 else 50
    independence_avg = independence_score / independence_count if independence_count > 0 else 50
    willpower_avg = willpower_score / willpower_count if willpower_count > 0 else 50
    
    # Calculate overall risk score with weighted formula
    # Weights based on importance for investment decisions
    weights = {
        'logic': 0.25,        # Analytical thinking
        'emotional': 0.30,    # Emotional stability (most important)
        'independence': 0.20, # Independence in decisions
        'willpower': 0.25     # Persistence and leadership
    }
    
    overall_score = (
        logic_avg * weights['logic'] +
        emotional_avg * weights['emotional'] +
        independence_avg * weights['independence'] +
        willpower_avg * weights['willpower']
    )
    
    # Round to nearest integer
    risk_score = int(round(overall_score))
    
    # Determine risk category
    if risk_score <= 30:
        risk_category = 'Conservative'
    elif risk_score <= 60:
        risk_category = 'Moderate'
    elif risk_score <= 80:
        risk_category = 'Growth'
    else:
        risk_category = 'Aggressive'
    
    # Generate asset allocation based on risk category
    asset_allocation = _generate_asset_allocation(risk_category)
    
    # Generate recommendations based on risk category
    recommendations = _generate_recommendations(risk_category)
    
    # Generate key traits based on scores
    key_traits = _generate_key_traits(logic_avg, emotional_avg, independence_avg, willpower_avg)
    
    return {
        'risk_score': risk_score,
        'risk_category': risk_category,
        'asset_allocation': asset_allocation,
        'recommendations': recommendations,
        'key_traits': key_traits
    }


def _generate_asset_allocation(risk_category: str) -> Dict[str, int]:
    """
    Generate asset allocation percentages based on risk category.
    
    Args:
        risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
    
    Returns:
        Dictionary with allocation percentages for stocks, bonds, cash, alternatives
    """
    allocations = {
        'Conservative': {
            'stocks': 20,
            'bonds': 50,
            'cash': 25,
            'alternatives': 5
        },
        'Moderate': {
            'stocks': 45,
            'bonds': 35,
            'cash': 15,
            'alternatives': 5
        },
        'Growth': {
            'stocks': 65,
            'bonds': 20,
            'cash': 10,
            'alternatives': 5
        },
        'Aggressive': {
            'stocks': 80,
            'bonds': 10,
            'cash': 5,
            'alternatives': 5
        }
    }
    
    return allocations.get(risk_category, allocations['Moderate'])


def _generate_recommendations(risk_category: str) -> List[str]:
    """
    Generate investment recommendations based on risk category.
    
    Args:
        risk_category: One of 'Conservative', 'Moderate', 'Growth', 'Aggressive'
    
    Returns:
        List of recommendation strings
    """
    recommendations = {
        'Conservative': [
            'Prioritize capital preservation over high returns',
            'Focus on government bonds and high-quality corporate bonds',
            'Maintain significant cash reserves for liquidity',
            'Consider dividend-paying blue-chip stocks',
            'Avoid speculative investments and high-volatility assets',
            'Regular portfolio rebalancing to maintain conservative allocation'
        ],
        'Moderate': [
            'Maintain balanced approach between growth and stability',
            'Diversify across different asset classes',
            'Include mix of growth and value stocks',
            'Invest in both government and corporate bonds',
            'Keep moderate cash reserves for opportunities',
            'Consider index funds for broad market exposure',
            'Review portfolio quarterly and rebalance annually'
        ],
        'Growth': [
            'Focus on capital appreciation with moderate risk',
            'Allocate significant portion to growth stocks',
            'Include emerging market investments',
            'Consider sector-specific ETFs for targeted exposure',
            'Maintain smaller cash position for tactical opportunities',
            'Use dollar-cost averaging for regular investments',
            'Monitor market conditions and adjust allocation accordingly'
        ],
        'Aggressive': [
            'Maximize growth potential with high-risk tolerance',
            'Heavy allocation to equities and growth stocks',
            'Include small-cap and international stocks',
            'Consider alternative investments (crypto, startups, etc.)',
            'Use leverage cautiously for enhanced returns',
            'Active trading and market timing strategies',
            'Accept higher volatility for potential higher returns'
        ]
    }
    
    return recommendations.get(risk_category, recommendations['Moderate'])


def _generate_key_traits(
    logic_avg: float,
    emotional_avg: float,
    independence_avg: float,
    willpower_avg: float
) -> List[str]:
    """
    Generate key personality traits based on category scores.
    
    Args:
        logic_avg: Average logic score (0-100)
        emotional_avg: Average emotional control score (0-100)
        independence_avg: Average independence score (0-100)
        willpower_avg: Average willpower score (0-100)
    
    Returns:
        List of trait strings
    """
    traits = []
    
    # Logic traits
    if logic_avg >= 70:
        traits.append('Analytical thinker')
    elif logic_avg >= 40:
        traits.append('Balanced decision-maker')
    else:
        traits.append('Intuitive decision-maker')
    
    # Emotional traits
    if emotional_avg >= 70:
        traits.append('Emotionally stable')
    elif emotional_avg >= 40:
        traits.append('Moderately emotional')
    else:
        traits.append('Emotionally reactive')
    
    # Independence traits
    if independence_avg >= 70:
        traits.append('Independent decision-maker')
    elif independence_avg >= 40:
        traits.append('Semi-independent')
    else:
        traits.append('Seeks external validation')
    
    # Willpower traits
    if willpower_avg >= 70:
        traits.append('Strong determination')
    elif willpower_avg >= 40:
        traits.append('Moderate persistence')
    else:
        traits.append('Needs motivation support')
    
    return traits


# TODO: This function will be replaced with AI service call in the future
def calculate_risk_score_with_ai(answers: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Placeholder for AI-based risk score calculation.
    
    This function will be implemented when AI service is integrated.
    It will call the AI service to analyze answers and generate
    personalized investment recommendations.
    
    Args:
        answers: List of dictionaries containing question_id and answer_value
    
    Returns:
        Dictionary with risk analysis results (same format as calculate_risk_score)
    
    TODO: Implement AI service integration
    """
    # For now, fall back to formula-based calculation
    return calculate_risk_score(answers)
