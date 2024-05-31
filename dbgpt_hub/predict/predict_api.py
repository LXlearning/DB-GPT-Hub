import os
import sys

sys.path.append('./')
from typing import Any, Dict, Optional

from dbgpt_hub.llm_base.chat_model import ChatModel
from dbgpt_hub.predict import predict


def start_predict(
    args: Optional[Dict[str, Any]] = None, cuda_visible_devices: Optional[str] = "0"
):
    # Setting CUDA Device
    os.environ["CUDA_VISIBLE_DEVICES"] = cuda_visible_devices

    # Default Arguments
    if args is None:
        args = {
            "model_name_or_path": "/data1/modules_huggingface/LLM/chatglm3-6b",
            "template": "chatglm3",
            "finetuning_type": "lora",
            "checkpoint_dir": "/data1/luox/ChatGLM-Finetuning/model/Cspider_sft_lora/epoch-9-step-1620",
            # "predict_file_path": "dbgpt_hub/data/eval_data/dev_sql.json",
            # "predict_out_dir": "dbgpt_hub/output/",
            "predicted_out_filename": "pred_sql.sql",
        }
    else:
        args = args

    # Execute prediction
    model = ChatModel(args)
    predict.predict(model)


if __name__ == "__main__":
    start_predict()
