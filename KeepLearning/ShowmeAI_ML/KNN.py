import numpy as np
import pandas as pd
from scipy.spatial import distance  # 用于计算欧式距离
from sklearn.preprocessing import StandardScaler  # 用于对数据进行标准化操作
from sklearn.neighbors import KNeighborsRegressor  # KNN算法
from sklearn.metrics import mean_squared_error  # 用于计算均方根误差

# %%
path = r"E:\ProSpace\VSCodePros\Python\KeepLearning\ShowmeAI_ML\data\rent_price.csv"
# path = "./data/rent_price.csv"
file = open(path, "r", encoding="gb18030", errors="ignore")
dc_listings = pd.read_csv(file)
features = [
    "accommodates",
    "bedrooms",
    "bathrooms",
    "beds",
    "price",
    "minimum_nights",
    "maximum_nights",
    "number_of_reviews",
]
dc_listings = dc_listings[features]

# %%
our_acc_value = 3
dc_listings["distance"] = np.abs(dc_listings.accommodates - our_acc_value)
dc_listings = dc_listings.sample(frac=1, random_state=0)
dc_listings = dc_listings.sort_values("distance")
dc_listings["price"] = (
    dc_listings["price"].str.replace(r"[$,]", "", regex=True).astype(float)
)
dc_listings = dc_listings.dropna()

# %%
dc_listings[features] = StandardScaler().fit_transform(dc_listings[features])
normalized_listings = dc_listings

# %%
# 取得训练集和测试集
norm_train_df = normalized_listings[:2792]
norm_test_df = normalized_listings[2792:]

# %%
# scipy包distance模块计算欧式距离
first_listings = normalized_listings.iloc[0][["accommodates", "bathrooms"]]
fifth_listings = normalized_listings.iloc[20][["accommodates", "bathrooms"]]


# 用python方法做多变量KNN模型
def predict_price_multivariate(new_listing_value, feature_columns):
    temp_df = norm_train_df
    # distance.cdist计算两个集合的距离
    temp_df["distance"] = distance.cdist(
        temp_df[feature_columns], [new_listing_value[feature_columns]]
    )
    temp_df = temp_df.sort_values("distance")  # temp_df按distance排序
    knn_5 = temp_df.price.iloc[:5]
    predicted_price = knn_5.mean()
    return predicted_price


cols = ["accommodates", "bathrooms"]
norm_test_df["predicted_price"] = norm_test_df[cols].apply(
    predict_price_multivariate, feature_columns=cols, axis=1
)
norm_test_df["squared_error"] = (
    norm_test_df["predicted_price"] - norm_test_df["price"]
) ** 2
mse = norm_test_df["squared_error"].mean()
rmse = mse ** (1 / 2)
print("python方法均方根误差: ", rmse)

# 利用sklearn完成KNN
col = ["accommodates", "bedrooms"]
knn = KNeighborsRegressor()
# 将自变量和因变量放入模型训练，并用测试数据测试
knn.fit(norm_train_df[cols], norm_train_df["price"])
two_features_predictions = knn.predict(norm_test_df[cols])
# 计算预测值与实际值的均方根误差
two_features_mse = mean_squared_error(norm_test_df["price"], two_features_predictions)
two_features_rmse = two_features_mse ** (1 / 2)
print("sklearn方法均方根误差: ", two_features_rmse)
# %%
