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

    art_2 = Fact('article-image-seg',
                 Article(
                     name='A review on image segmentation techniques',
                     authors='Nikhil R., Sankar K.',
                     year='1993',
                     url='https://www.sciencedirect.com/science/article/abs/pii/003132039390135J'))

    art_3 = Fact('article-mlp',
                 Article(
                    name='Multilayer Perceptron Tutorial',
                    authors='Leonardo Noregia',
                    year='2005',
                    url='http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.608.2530&rep=rep1&type=pdf'
                 ))

    art_4 = Fact('article-cnn',
                 Article(
                    name='An Introduction to Convolutional Neural Networks',
                    authors='Keiron O\'Shea, Ryan Nash',
                    year='2015',
                    url='https://arxiv.org/abs/1511.08458'
                 ))

    art_5 = Fact('article-seg-cnn',
                 Article(
                    name='DRINet for Medical Images Segmentation',
                    authors='Liand Chen, Pzul Bentley, Kensaku Mori et al.',
                    year='2018',
                    url='https://ieeexplore.ieee.org/abstract/document/8357580'
                 ))

    art_6 = Fact('article-img-compl-cnn',
                 Article(
                    name='Globally and locally consistent image completion',
                    authors='Satoshi lizuka, Edgar Simo-Serra, Iroshi Ishikawa',
                    year='2017',
                    url='https://dl.acm.org/doi/abs/10.1145/3072959.3073659'
                 ))

    art_7 = Fact('article-img-compr-vae',
                 Article(
                    name='Efficient image encryption and compression based on a VAE generative model',
                    authors='Xintao Duan, Jinjing Liu, En Zhang',
                    year='2019',
                    url='https://link.springer.com/article/10.1007/s11554-018-0826-4'
                 ))

    art_8 = Fact('article-img-gen-rec-sup-vae',
                 Article(
                    name='Generating Diverse High-Fidelity Images with VQ-VAE-2',
                    authors='Ali Razavi, Aaron van den Oord, Oriol Vinyals',
                    year='2019',
                    url='https://proceedings.neurips.cc/paper/2019/hash/5f8e2fa1718d1bbcadf1cd9c7a54fb8c-Abstract.html'
                 ))

    art_9 = Fact('article-img-gen-rec-low-vae',
                 Article(
                    name='Understanding disentangling in β-VAE',
                    authors='Christopher P. Burgess, Irina Higgins, Arka Pal, Loic Matthey, Nick Watters, Guillaume Desjardins, Alexander Lerchner',
                    year='2018',
                    url='https://arxiv.org/abs/1804.03599'
                 ))

    art_10 = Fact('article-img-gen-gan',
                 Article(
                    name='GAN-based synthetic brain MR image generation',
                    authors='Changhee Han, Hideaki Hayashi, Leonardo Rundo, Ryosuke Araki, Wataru Shimoda, Shinichi Muramatsu, Yujiro Furukawa',
                    year='2018',
                    url='https://ieeexplore.ieee.org/abstract/document/8363678'
                 ))

    art_11 = Fact('article-son-class-cnn',
                 Article(
                    name='Deep Convolutional Neural Networks and Data Augmentation for Environmental Sound Classification',
                    authors='Justin Salamon, Juan Pablo Bello',
                    year='2017',
                    url='https://ieeexplore.ieee.org/abstract/document/7829341'
                 ))

    art_12 = Fact('article-son-seg-cnn',
                 Article(
                    name='A study of time-frequency features for CNN-based automatic heart sound classification for pathology detection',
                    authors='Baris Botzkurt, Ioannis Germanakis, Yannis Stylianou',
                    year='2018',
                    url='https://www.sciencedirect.com/science/article/abs/pii/S0010482518301744'
                 ))

    art_13 = Fact('article-son-seg-rnn',
                 Article(
                    name='Sound event aware environmental sound segmentation with Mask U-Net',
                    authors='Y Sudo, K Itoyama, K Nishida, K Nakadia',
                    year='2020',
                    url='https://www.tandfonline.com/doi/abs/10.1080/01691864.2020.1829040'
                 ))

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
    system.addRule((in_img & nn_cnn_mlp).give(art_2))
    return system
