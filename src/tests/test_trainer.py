import sys
sys.path.append("./../")
from transformers import AutoTokenizer
from trainers.trainer import Trainer
from trainers.seq2seq_trainer import Seq2SeqTrainer
from models.rnn_models import Seq2Seq
from models.nmt_models import BartForNMT, T5ForNMT
import torch

# model = BartModel.from_pretrained('facebook/bart-base')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


config = {
    "model_name": "bart_nmt",
    "src_max_length": 183,
    "dst_max_length": 208,
    "src_vocab_size": 31102,
    "dst_vocab_size": 28996,
    "enc_hidden_dim": 8,
    "dec_hidden_dim": 8,
    "max_epochs": 10,
    "batch_size": 4,
    "seed": 7
}


model = BartForNMT(768, 50265)
# model = Seq2Seq(config["src_vocab_size"],
#                 config["dst_vocab_size"],
#                 config["enc_hidden_dim"],
#                 config["dec_hidden_dim"],
#                 1, 1, 0.5, device)

src_tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-italian-cased")
dst_tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
trainer = Trainer(model, src_tokenizer, dst_tokenizer, config)
trainer.train()