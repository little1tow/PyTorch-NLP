from torchnlp.datasets.reverse import reverse_dataset
from torchnlp.datasets.count import count_dataset
from torchnlp.datasets.zero import zero_dataset
from torchnlp.datasets.simple_qa import simple_qa_dataset
from torchnlp.datasets.imdb import imdb_dataset
from torchnlp.datasets.wikitext_2 import wikitext_2_dataset
from torchnlp.datasets.penn_treebank import penn_treebank_dataset
from torchnlp.datasets.ud_pos import ud_pos_dataset
from torchnlp.datasets.snli import snli_dataset
from torchnlp.datasets.dataset import Dataset

__all__ = [
    'Dataset',
    'snli_dataset',
    'simple_qa_dataset',
    'imdb_dataset',
    'wikitext_2_dataset',
    'penn_treebank_dataset',
    'ud_pos_dataset',
    'reverse_dataset',
    'count_dataset',
    'zero_dataset',
]
