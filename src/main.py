from src.AkiNN import AkiNN
from src.Fact import *


def initialize_akinn():
    system = AkiNN()

    # Ce qu'on veut traiter
    in_img = Fact('entree-image', 'Je travaille avec des images')
    in_son = Fact('entree-son', 'Je travaille avec des sons')
    in_phrase = Fact('entree-phrase', 'Je travaille avec des phrases')
    in_txt = Fact('entree-texte', 'Je travaille avec des textes')
    in_mot = Fact('entree-mot')
    in_video = Fact('entree-video')
    in_vec = Fact('entree-vecteur')
    in_mat = Fact('entree-matrice')

    temp = Fact('temporalite')

    # Ce qu'on veut faire
    act_class = Fact('action-classification')
    act_seg = Fact('action-segmentation')
    act_reg = Fact('action-regression')
    act_compl = Fact('action-completion')
    act_compr = Fact('action-compression')
    act_gen = Fact('action-generation')
    act_feat = Fact('action-features')

    gen_like = Fact('generation-ressemble')
    gen_new = Fact('generation-nouveau')

    rec_sup = Fact('reconstruction-elevee')

    # Ce qu'on a
    bdd_label = Fact('bdd-etiquetee')
    bdd_unlabel = Fact('bdd-non-etiquetee')

    class_bin = Fact('classes-binaire')
    class_mul = Fact('classes-multiple')

    # Ce qu'on peut obtenir
    nn_perc = Fact('reseau-perceptron', 'Perceptron', fact_type='terminal')
    nn_mlp = Fact('reseau-mlp', 'Perceptron multi-couches', fact_type='terminal')
    nn_cnn = Fact('reseau-cnn', 'Réseau de neurones convolutif', fact_type='terminal')
    nn_cnn_mlp = Fact('reseau-cnn+mlp', 'Réseau de neurones convolutif suivi d\'un perceptron multi-couches', fact_type='terminal')
    nn_rnn = Fact('reseau-rnn', fact_type='terminal')
    nn_rnn_mlp = Fact('reseau-rnn+mlp', fact_type='terminal')
    nn_hopf = Fact('reseau-hopf', fact_type='terminal')
    nn_bolt = Fact('reseau-boltzmann', fact_type='terminal')
    nn_ae = Fact('reseau-autoencoder', fact_type='terminal')
    nn_vae = Fact('reseau-vae', fact_type='terminal')
    nn_gan = Fact('reseau-gan', fact_type='terminal')

    art_1 = Fact('article-perceptron',
                 Article(
                     name='The perceptron: a probabilistic model for information storage and organization in the brain',
                     authors='F. Rosenblatt',
                     year='1998',
                     url='https://psycnet.apa.org/journals/rev/65/6/386/'))

    beta_high = Fact('parametre-beta-grand')
    beta_low = Fact('parametre-beta-petit')

    system.addRule((in_img & temp).give(in_video))

    system.addRule((in_img & act_class).give(nn_cnn_mlp))
    system.addRule((in_img & act_class).give(nn_mlp))
    system.addRule((in_img & act_seg).give(nn_cnn))
    system.addRule((in_img & act_compl).give(nn_rnn))

    system.addRule((in_img & act_compr).give(nn_vae))
    system.addRule((in_img & act_gen & rec_sup).give(nn_vae))
    system.addRule(Rule(rec_sup).give(beta_low))
    system.addRule((in_img & act_gen & neg(rec_sup)).give(nn_gan))
    system.addRule((in_img & act_gen & neg(rec_sup)).give(nn_vae))
    system.addRule(Rule(neg(rec_sup)).give(beta_high))

    system.addRule((in_son & act_class).give(nn_cnn_mlp))
    system.addRule((in_son & act_class).give(nn_mlp))
    system.addRule((in_son & act_seg).give(nn_cnn))
    system.addRule((in_son & act_seg).give(nn_rnn))
    system.addRule((in_son & act_compr).give(nn_vae))
    system.addRule((in_son & act_compl).give(nn_rnn))
    system.addRule((in_son & act_gen).give(nn_rnn))
    system.addRule((in_son & act_gen).give(nn_gan))

    system.addRule((in_phrase & act_class).give(nn_mlp))
    system.addRule((in_phrase & act_class).give(nn_cnn))
    system.addRule((in_phrase & act_compl).give(nn_rnn))
    system.addRule((in_phrase & act_gen).give(nn_rnn))
    system.addRule((in_phrase & act_gen).give(nn_gan))

    system.addRule((in_txt & act_class).give(nn_rnn))
    system.addRule((in_txt & act_class).give(nn_cnn))
    system.addRule((in_txt & act_seg).give(nn_rnn))
    system.addRule((in_txt & act_seg).give(nn_cnn))
    system.addRule((in_txt & act_compl).give(nn_rnn))
    system.addRule((in_txt & act_compr).give(nn_rnn))
    system.addRule((in_txt & act_gen).give(nn_rnn))

    system.addRule((in_video & act_class).give(nn_rnn))
    system.addRule((in_video & act_class).give(nn_cnn))
    system.addRule((in_video & act_seg).give(nn_rnn))
    system.addRule((in_video & act_compl).give(nn_cnn))
    system.addRule((in_video & act_compl).give(nn_gan))
    system.addRule((in_video & act_compr).give(nn_rnn))
    system.addRule((in_video & act_gen).give(nn_gan))

    system.addRule(Rule(in_mat).give(in_vec))
    system.addRule((in_vec & act_reg).give(nn_rnn))
    system.addRule((in_vec & act_class).give(nn_cnn))
    system.addRule((in_vec & act_seg).give(nn_rnn))
    system.addRule((in_vec & act_compl).give(nn_cnn))
    system.addRule((in_vec & act_compl).give(nn_gan))
    system.addRule((in_vec & act_compr).give(nn_rnn))
    system.addRule((in_vec & act_gen).give(nn_gan))

    # ajout de la bibliographie
    system.addRule(Rule(nn_perc).give(art_1))

    return system
