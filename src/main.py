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

    not_here = Fact('pas_ici', 'Faut pas faire du réseau de neurones là...', fact_type='terminal')

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

    art_6 = Fact('article-img-compl-rnn',
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

    art_14 = Fact('article-video-seg-rnn',
                 Article(
                     name='Tensor-Train Recurrent Neural Networks for Video Classification',
                     authors='Yang Y. at al.',
                     year='2017',
                     url='https://arxiv.org/abs/1707.01786'))

    art_15 = Fact('article-video-class',
                 Article(
                     name="Large scale video classification with convolutional neural networks",
                     authors='Karpathy A. & al.',
                     year='2014',
                     url='https://www.cv-foundation.org/openaccess/content_cvpr_2014/papers/Karpathy_Large-scale_Video_Classification_2014_CVPR_paper.pdf'
                 ))

    art_16 = Fact('article-video-segm-rnn',
                 Article(
                     name="Recurrent Fully Convolutional Networks for Video Segmentation",
                     authors='Valipour S. & al.',
                     year='2017',
                     url='https://ieeexplore.ieee.org/abstract/document/7926594'
                 ))

    art_17 = Fact('article-video-segm-cnn',
                 Article(
                     name="Spatiotemporal CNN for Video Object Segmentation",
                     authors='Xu K. & al.',
                     year='2019',
                     url='https://openaccess.thecvf.com/content_CVPR_2019/html/Xu_Spatiotemporal_CNN_for_Video_Object_Segmentation_CVPR_2019_paper.html'
                 ))

    art_18 = Fact('article-video-compl-cnn',
                 Article(
                     name="Deep Video Generation, Prediction and Completion of Human Action Sequences",
                     authors='Haoye C. & al.',
                     year='2018',
                     url='https://openaccess.thecvf.com/content_ECCV_2018/html/Chunyan_Bai_Deep_Video_Generation_ECCV_2018_paper.html'
                 ))

    art_19 = Fact('article-video-compl-cnn',
                 Article(
                     name="Deep Video Generation, Prediction and Completion of Human Action Sequences",
                     authors='Haoye C. & al.',
                     year='2018',
                     url='https://openaccess.thecvf.com/content_ECCV_2018/html/Chunyan_Bai_Deep_Video_Generation_ECCV_2018_paper.html'
                 ))

    art_20 = Fact('article-text-classi-rnn',
                 Article(
                     name="Generative and Discriminative Text Classification with Recurrent Neural Networks",
                     authors='Yogatam D. & al.',
                     year='2017',
                     url='https://arxiv.org/pdf/1703.01898.pdf'
                 ))

    art_21 = Fact('article-text-classi-cnn',
                 Article(
                     name="Densely Connected CNN with Multi-scale Feature Attention for Text Classification",
                     authors='Wang S. & al.',
                     year='2019',
                     url='https://www.researchgate.net/profile/Zhidong_Deng/publication/326203796_Densely_Connected_CNN_with_Multi-scale_Feature_Attention_for_Text_Classification/links/5bd1f6a04585150b2b875474/Densely-Connected-CNN-with-Multi-scale-Feature-Attention-for-Text-Classification.pdf'
                 ))

    art_22 = Fact('article-text-seg-rnn',
                 Article(
                     name="Paragraph text segmentation into lines with Recurrent Neural Networks",
                     authors='Moysset B. & al.',
                     year='2015',
                     url='https://ieeexplore.ieee.org/abstract/document/7333803'
                 ))

    art_23 = Fact('article-text-compl-rnn',
                 Article(
                     name="Word RNN as a Baseline for Sentence Completion",
                     authors='Heewoong P. & al.',
                     year='2018',
                     url='https://ieeexplore.ieee.org/abstract/document/8596572/'
                 ))

    art_24 = Fact('article-text-compl-cnn',
                 Article(
                     name="Neural Networks for Text Correction and Completion in Keyboard Decoding",
                     authors='Gosh S. & al.',
                     year='2017',
                     url='https://arxiv.org/abs/1709.06429'
                 ))

    art_25 = Fact('article-text-compr-rnn',
                 Article(
                     name="Pushing the limits of RNN Compression",
                     authors='Thakker U. & al.',
                     year='2019',
                     url='https://arxiv.org/abs/1910.02558'
                 ))

    art_26 = Fact('article-text-compr-cnn',
                 Article(
                     name="Dictionary based Compression Type Classification using a CNN Architecture",
                     authors='Hyewon S. & al.',
                     year='2019',
                     url='https://ieeexplore.ieee.org/abstract/document/9023258'
                 ))

    art_27 = Fact('article-text-gen-rnn',
                 Article(
                     name="Story Scrambler - Automatic Text Generation Using Word Level RNN-LSTM",
                     authors='Pawade D. & al.',
                     year='2018',
                     url='https://pdfs.semanticscholar.org/c51d/13034b2df47dae8f33bd0efad996de99ed4c.pdf'
                 ))

    art_28 = Fact('article-son-gen-gan',
                 Article(
                     name="MelGAN: Generative Adversarial Networks for Conditional Waveform Synthesis",
                     authors='Kundan K. & al.',
                     year='2019',
                     url='https://proceedings.neurips.cc/paper/2019/hash/6804c9bca0a615bdb9374d00a9fcba59-Abstract.html'
                 ))

    art_29 = Fact('article-son-gen-rnn',
                 Article(
                     name="Automated sound generation based on image colour spectrum with using the recurrent neural network",
                     authors='Nikitin N.A. & al.',
                     year='2019',
                     url='http://ceur-ws.org/Vol-2212/paper53.pdf'
                 ))

    art_30 = Fact('article-son-compr-vae',
                 Article(
                     name="Anaesthesia for neurosurgery in the sitting position: a practical approach",
                     authors='Domaingue CM. & al.',
                     year='2005',
                     url='https://journals.sagepub.com/doi/abs/10.1177/0310057X0503300307'
                 ))

    beta_high = Fact('parametre-beta-grand')
    beta_low = Fact('parametre-beta-petit')

    system.addRule((bdd_label & in_img & temp).give(in_video))

    system.addRule((bdd_label & in_img & act_class).give(nn_cnn_mlp))
    system.addRule((bdd_label & in_img & act_class).give(nn_mlp))
    system.addRule((bdd_label & in_img & act_seg).give(nn_cnn))
    system.addRule((bdd_label & in_img & act_compl).give(nn_rnn))

    system.addRule((bdd_label & in_img & act_compr).give(nn_vae))
    system.addRule((bdd_label & in_img & act_gen & rec_sup).give(nn_vae))
    system.addRule(Rule(rec_sup).give(beta_low))
    system.addRule((bdd_label & in_img & act_gen & neg(rec_sup)).give(nn_gan))
    system.addRule((bdd_label & in_img & act_gen & neg(rec_sup)).give(nn_vae))
    system.addRule(Rule(neg(rec_sup)).give(beta_high))

    system.addRule((bdd_label & in_son & act_class).give(nn_cnn_mlp))
    system.addRule((bdd_label & in_son & act_class).give(nn_mlp))
    system.addRule((bdd_label & in_son & act_seg).give(nn_cnn))
    system.addRule((bdd_label & in_son & act_seg).give(nn_rnn))
    system.addRule((bdd_label & in_son & act_compr).give(nn_vae))
    system.addRule((bdd_label & in_son & act_compl).give(nn_rnn))
    system.addRule((bdd_label & in_son & act_gen).give(nn_rnn))
    system.addRule((bdd_label & in_son & act_gen).give(nn_gan))

    system.addRule((bdd_label & in_phrase & act_class).give(nn_mlp))
    system.addRule((bdd_label & in_phrase & act_class).give(nn_cnn))
    system.addRule((bdd_label & in_phrase & act_compl).give(nn_rnn))
    system.addRule((bdd_label & in_phrase & act_gen).give(nn_rnn))
    system.addRule((bdd_label & in_phrase & act_gen).give(nn_gan))

    system.addRule((bdd_label & in_txt & act_class).give(nn_rnn))
    system.addRule((bdd_label & in_txt & act_class).give(nn_cnn))
    system.addRule((bdd_label & in_txt & act_seg).give(nn_rnn))
    system.addRule((bdd_label & in_txt & act_seg).give(nn_cnn))
    system.addRule((bdd_label & in_txt & act_compl).give(nn_rnn))
    system.addRule((bdd_label & in_txt & act_compr).give(nn_cnn))
    system.addRule((bdd_label & in_txt & act_gen).give(nn_rnn))

    system.addRule((bdd_label & in_video & act_class).give(nn_rnn))

    system.addRule((bdd_label & in_video & act_class).give(nn_cnn))
    system.addRule((bdd_label & in_video & act_seg).give(nn_rnn))
    system.addRule((bdd_label & in_video & act_compl).give(nn_cnn))
    system.addRule((bdd_label & in_video & act_compl).give(nn_gan))
    system.addRule((bdd_label & in_video & act_compr).give(nn_rnn))
    system.addRule((bdd_label & in_video & act_gen).give(nn_gan))

    system.addRule(Rule(in_mat).give(in_vec))
    system.addRule((bdd_label & in_vec & act_reg).give(nn_rnn))
    system.addRule((bdd_label & in_vec & act_class).give(nn_cnn))
    system.addRule((bdd_label & in_vec & act_seg).give(nn_rnn))
    system.addRule((bdd_label & in_vec & act_compl).give(nn_cnn))
    system.addRule((bdd_label & in_vec & act_compl).give(nn_gan))
    system.addRule((bdd_label & in_vec & act_compr).give(nn_rnn))
    system.addRule((bdd_label & in_vec & act_gen).give(nn_gan))

    system.addRule(Rule(bdd_unlabel).give(not_here))

    # ajout de la bibliographie
    system.addRule(Rule(nn_perc).give(art_1))
    system.addRule((in_img & nn_cnn_mlp).give(art_2))

    system.addRule((in_img & nn_mlp).give(art_3))
    system.addRule((in_img & nn_cnn).give(art_5))
    system.addRule((in_img & nn_rnn).give(art_6))

    system.addRule((in_img & act_compr & nn_vae).give(art_7))
    system.addRule((in_img & rec_sup & nn_vae).give(art_8))
    system.addRule((in_img & neg(rec_sup) & nn_vae).give(art_9))
    system.addRule((in_img & nn_gan).give(art_10))

    system.addRule((in_son & act_compr & nn_vae).give(art_30))
    system.addRule((in_son & act_gen & nn_rnn).give(art_29))
    system.addRule((in_son & act_gen & nn_gan).give(art_28))

    system.addRule((in_txt & act_gen & nn_rnn).give(art_27))
    system.addRule((in_txt & act_compr & nn_cnn).give(art_26))
    system.addRule((in_txt & act_compr & nn_rnn).give(art_25))
    system.addRule((in_txt & act_compl & nn_cnn).give(art_24))
    system.addRule((in_txt & act_compl & nn_rnn).give(art_23))
    system.addRule((in_txt & act_seg & nn_rnn).give(art_22))
    system.addRule((in_txt & act_class & nn_cnn).give(art_21))
    system.addRule((in_txt & act_class & nn_rnn).give(art_20))

    system.addRule((in_video & act_compl & nn_cnn).give(art_19))
    system.addRule((in_video & act_seg & nn_cnn).give(art_17))
    system.addRule((in_video & act_seg & nn_rnn).give(art_16))
    system.addRule((in_video & act_class & nn_cnn).give(art_15))
    system.addRule((in_video & act_seg & nn_rnn).give(art_14))
    system.addRule((in_son & act_seg & nn_rnn).give(art_13))
    system.addRule((in_son & act_seg & nn_cnn).give(art_12))
    system.addRule((in_son & nn_cnn_mlp).give(art_11))


    return system
