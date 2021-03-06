# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Init module for TensorFlow Data Validation."""

# Import stats API.
from tensorflow_data_validation.api.stats_api import GenerateStatistics

# Import validation API.
from tensorflow_data_validation.api.validation_api import infer_schema
from tensorflow_data_validation.api.validation_api import validate_statistics

# Import coders.
from tensorflow_data_validation.coders.csv_decoder import DecodeCSV
from tensorflow_data_validation.coders.tf_example_decoder import TFExampleDecoder

# Import stats generators.
from tensorflow_data_validation.statistics.generators.stats_generator import CombinerStatsGenerator
from tensorflow_data_validation.statistics.generators.stats_generator import TransformStatsGenerator

# Import stats options.
from tensorflow_data_validation.statistics.stats_options import StatsOptions

# Import display utilities.
from tensorflow_data_validation.utils.display_util import display_anomalies
from tensorflow_data_validation.utils.display_util import display_schema
from tensorflow_data_validation.utils.display_util import visualize_statistics

# Import schema utilities.
from tensorflow_data_validation.utils.schema_util import get_domain
from tensorflow_data_validation.utils.schema_util import get_feature
from tensorflow_data_validation.utils.schema_util import load_schema_text
from tensorflow_data_validation.utils.schema_util import set_domain
from tensorflow_data_validation.utils.schema_util import write_schema_text

# Import stats lib.
from tensorflow_data_validation.utils.stats_gen_lib import generate_statistics_from_csv
from tensorflow_data_validation.utils.stats_gen_lib import generate_statistics_from_dataframe
from tensorflow_data_validation.utils.stats_gen_lib import generate_statistics_from_tfrecord
from tensorflow_data_validation.utils.stats_gen_lib import load_statistics

# Import version string.
from tensorflow_data_validation.version import __version__
