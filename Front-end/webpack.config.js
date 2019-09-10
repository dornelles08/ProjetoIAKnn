module.exports = {
    entry: ['@babel/polyfill', './src/main.js'], // carrega o polyfill antes de carregar o main.
    output: {
        path: __dirname + '/public',
        filename: 'bundle.js'
    },
    devServer: {
        // Caminho onde deve abrir o servidor da aplicação.
        // geralmente o caminho é onde fica o index.html
        contentBase: __dirname + '/public'
        // Alterar tambem o package.json
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader' // para isso funcionar, tem q instalar... yarn add babel-loader -D
                    // Trocar no package.json para executar o webpack ao inves do babel.
                }
            }
        ]
    }
};