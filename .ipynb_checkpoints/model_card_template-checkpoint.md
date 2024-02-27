# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

I used linear regression for this model without performing any hyperparameter tuning.  Specifically, I utilized RBF with SVC. RBF is a Gaussian kernel. 

## Intended Use

The intended use of this current model is to look at different categories in a dataframe, and predict whether an individual's income is greater than; or less than or equal to 50,000 USD

The purpose of this model is to look at different categories within a dataframe and predict whether an individual's income exceeds $50,000 or is less than or equal to that amount.

## Training Data

We used census data from UC Irvine, stored in csv.  We utilized OneHotEncoder, LabelBinarizer, and used ravel() to convert the data into a single-dimensional array.

## Evaluation Data

We ran the test of the data on just 30 percent of the original.  We utilized the same methods as previously.

## Metrics
The metrics were as follows:
Precision: 0.9884 | Recall: 0.1469 | F1: 0.2558

## Ethical Considerations

There may be existing bias on the method of data collection from the census and categorization of salary based on race may be seen as insensitive or unethical.  It's important to consider that while there may be correlation within categories for salary predictions, it doesn't necessarily insinuate a cause/effect relationship of any one category or combination of categories.

## Caveats and Recommendations
If we were to do this differently, I would utilize Random Forest over RBF.  Random Forest is more efficient with larger data sets like the one utilized in this project.

I would be curious to analyze the correlation between hours-worked-over-40-hours and salary, and it would be more interesting to see the actual salary to the dollar.