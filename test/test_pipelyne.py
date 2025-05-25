import pandas as pd
import pandas.testing as pdt
from app.pipeline.transform import concat_data_frames

df1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def test_concat_data_frames():
    # Arrange: concatena manualmente numa lista
    expected = pd.concat([df1, df2], ignore_index=True)
    # Act: usa nossa função, que já espera uma lista
    result   = concat_data_frames([df1, df2])
    # Assert: compara DataFrames
    pdt.assert_frame_equal(result, expected)
