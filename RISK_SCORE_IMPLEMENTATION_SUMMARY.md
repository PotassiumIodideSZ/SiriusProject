# Risk Score Implementation Summary

## Overview
This document summarizes the implementation of the risk score calculation and investment recommendation system for the Sirius Investment Platform.

## Implementation Details

### Phase 1: Backend Changes (Without AI)

#### 1. Database Models

**File: [`SiriusBackend/recommendations/models.py`](SiriusBackend/recommendations/models.py)**

Created `InvestmentProfile` model with the following fields:
- `user`: One-to-one relationship with User (stores latest result only)
- `risk_score`: Integer (0-100)
- `risk_category`: Enum (Conservative, Moderate, Growth, Aggressive)
- `asset_allocation`: JSON object with allocation percentages
- `recommendations`: JSON array of recommendation strings
- `key_traits`: JSON array of personality trait strings
- `created_at`, `updated_at`: Timestamps

#### 2. Risk Calculator

**File: [`SiriusBackend/surveys/risk_calculator.py`](SiriusBackend/surveys/risk_calculator.py)**

Implemented formula-based risk calculation with:
- **Logic & Reasoning (Questions 1-7)**: Weight 25%
- **Emotional Control (Questions 8-12)**: Weight 30% (most important)
- **Independence (Questions 13-17)**: Weight 20%
- **Willpower & Leadership (Questions 18-23)**: Weight 25%

Key functions:
- `calculate_risk_score(answers)`: Main calculation function
- `_generate_asset_allocation(risk_category)`: Returns allocation based on category
- `_generate_recommendations(risk_category)`: Returns 5-7 recommendations
- `_generate_key_traits(...)`: Returns personality traits based on scores
- `calculate_risk_score_with_ai(answers)`: Placeholder for future AI integration

#### 3. API Views

**File: [`SiriusBackend/surveys/views.py`](SiriusBackend/surveys/views.py)**

Updated `SurveySubmitView.post()` to:
1. Accept survey answers
2. Calculate risk profile using `calculate_risk_score()`
3. Create/update `InvestmentProfile` for the user (only latest result)
4. Return complete risk profile in response

**File: [`SiriusBackend/recommendations/views.py`](SiriusBackend/recommendations/views.py)**

Added `InvestmentProfileView`:
- GET `/api/recommendations/profile/`
- Returns user's latest investment profile
- Returns 404 if no profile exists

#### 4. Serializers

**File: [`SiriusBackend/recommendations/serializers.py`](SiriusBackend/recommendations/serializers.py)**

Created `InvestmentProfileSerializer` with all profile fields.

#### 5. URL Configuration

**File: [`SiriusBackend/recommendations/urls.py`](SiriusBackend/recommendations/urls.py)**

Added investment profile endpoint:
```python
path('profile/', InvestmentProfileView.as_view(), name='investment-profile')
```

### Phase 2: Frontend Changes

#### 1. Survey Store

**File: [`SiriusFrontend/SiriusVue/src/features/survey/stores/surveyStore.js`](SiriusFrontend/SiriusVue/src/features/survey/stores/surveyStore.js)**

Updated `finishSurvey()` to:
- Store risk profile data in localStorage after survey submission
- Pass data to results page

#### 2. Results API Service

**File: [`SiriusFrontend/SiriusVue/src/features/results/services/resultsAPI.js`](SiriusFrontend/SiriusVue/src/features/results/services/resultsAPI.js)**

Added new methods:
- `getInvestmentProfile()`: Fetch profile from API
- `getInvestmentProfileFromStorage()`: Get from localStorage
- `clearInvestmentProfileFromStorage()`: Clear localStorage

#### 3. Results Store

**File: [`SiriusFrontend/SiriusVue/src/features/results/stores/resultsStore.js`](SiriusFrontend/SiriusVue/src/features/results/stores/resultsStore.js)**

Added new state and methods:
- `riskCategory`, `assetAllocation`, `keyTraits` state
- `fetchInvestmentProfile()`: Fetch from API
- `loadInvestmentProfileFromStorage()`: Load from localStorage

#### 4. Results Composable

**File: [`SiriusFrontend/SiriusVue/src/features/results/composables/useResults.js`](SiriusFrontend/SiriusVue/src/features/results/composables/useResults.js)**

Added new computed properties and methods:
- `riskCategory`, `assetAllocation`, `keyTraits` computed
- `fetchInvestmentProfile()`, `loadInvestmentProfileFromStorage()` methods

#### 5. Results View

**File: [`SiriusFrontend/SiriusVue/src/features/results/components/ResultsView.vue`](SiriusFrontend/SiriusVue/src/features/results/components/ResultsView.vue)**

Enhanced to display:
- Risk score with circular progress bar
- Risk category badge with color coding
- Key personality traits
- Investment recommendations list
- Asset allocation percentages (stocks, bonds, cash, alternatives)
- Loading and error states

#### 6. Constants

**File: [`SiriusFrontend/SiriusVue/src/core/config/constants.js`](SiriusFrontend/SiriusVue/src/core/config/constants.js)**

Added:
- `API_ENDPOINTS.RESULTS.INVESTMENT_PROFILE`: `/recommendations/profile/`
- `STORAGE_KEYS.RISK_PROFILE`: `riskProfile`

## Risk Categories and Allocations

### Conservative (0-30%)
- Focus on capital preservation
- Allocation: Stocks 20%, Bonds 50%, Cash 25%, Alternatives 5%
- 6 recommendations

### Moderate (31-60%)
- Balanced growth and stability
- Allocation: Stocks 45%, Bonds 35%, Cash 15%, Alternatives 5%
- 7 recommendations

### Growth (61-80%)
- Focus on capital appreciation
- Allocation: Stocks 65%, Bonds 20%, Cash 10%, Alternatives 5%
- 7 recommendations

### Aggressive (81-100%)
- Maximum growth potential with high risk
- Allocation: Stocks 80%, Bonds 10%, Cash 5%, Alternatives 5%
- 7 recommendations

## Data Flow

1. **Survey Submission**:
   - User completes 23-question survey
   - Frontend sends answers to `/api/surveys/submit/`
   - Backend calculates risk score using formula
   - Backend creates/updates `InvestmentProfile` for user
   - Backend returns complete risk profile
   - Frontend stores profile in localStorage
   - Frontend redirects to `/results`

2. **Results Display**:
   - Results page loads
   - First tries to load from localStorage (from survey submission)
   - If not in storage, fetches from `/api/recommendations/profile/`
   - Displays all profile data (score, category, allocation, recommendations, traits)

## Future AI Integration

The implementation is designed to easily integrate AI-based analysis:

1. **Placeholder Function**: [`calculate_risk_score_with_ai()`](SiriusBackend/surveys/risk_calculator.py:258) in `risk_calculator.py`
2. **Easy Replacement**: Replace formula-based call with AI service call
3. **Caching**: Can add caching layer for AI responses
4. **Same Interface**: Frontend doesn't need changes

## Testing Checklist

- [ ] Submit survey and verify risk score calculation
- [ ] Check investment profile is saved in database
- [ ] Verify results page displays correctly
- [ ] Test localStorage fallback
- [ ] Test API endpoint `/api/recommendations/profile/`
- [ ] Verify only latest profile is stored per user
- [ ] Test all risk categories (Conservative, Moderate, Growth, Aggressive)
- [ ] Verify asset allocation percentages
- [ ] Check recommendations are appropriate for each category
- [ ] Test error handling (no profile, API errors)

## Files Modified/Created

### Backend
- [`SiriusBackend/recommendations/models.py`](SiriusBackend/recommendations/models.py) - Added InvestmentProfile model
- [`SiriusBackend/surveys/risk_calculator.py`](SiriusBackend/surveys/risk_calculator.py) - Created risk calculator
- [`SiriusBackend/surveys/views.py`](SiriusBackend/surveys/views.py) - Updated SurveySubmitView
- [`SiriusBackend/recommendations/views.py`](SiriusBackend/recommendations/views.py) - Added InvestmentProfileView
- [`SiriusBackend/recommendations/serializers.py`](SiriusBackend/recommendations/serializers.py) - Added InvestmentProfileSerializer
- [`SiriusBackend/recommendations/urls.py`](SiriusBackend/recommendations/urls.py) - Added profile endpoint

### Frontend
- [`SiriusFrontend/SiriusVue/src/features/survey/stores/surveyStore.js`](SiriusFrontend/SiriusVue/src/features/survey/stores/surveyStore.js) - Updated finishSurvey
- [`SiriusFrontend/SiriusVue/src/features/results/services/resultsAPI.js`](SiriusFrontend/SiriusVue/src/features/results/services/resultsAPI.js) - Added profile methods
- [`SiriusFrontend/SiriusVue/src/features/results/stores/resultsStore.js`](SiriusFrontend/SiriusVue/src/features/results/stores/resultsStore.js) - Added profile state
- [`SiriusFrontend/SiriusVue/src/features/results/composables/useResults.js`](SiriusFrontend/SiriusVue/src/features/results/composables/useResults.js) - Added profile methods
- [`SiriusFrontend/SiriusVue/src/features/results/components/ResultsView.vue`](SiriusFrontend/SiriusVue/src/features/results/components/ResultsView.vue) - Enhanced display
- [`SiriusFrontend/SiriusVue/src/core/config/constants.js`](SiriusFrontend/SiriusVue/src/core/config/constants.js) - Added endpoints and keys

## Notes

- All calculations are currently formula-based (no AI)
- Only the latest investment profile is stored per user
- Results are displayed with simple numbers (no charts)
- Russian labels are used in the frontend
- The system is ready for AI integration when needed
