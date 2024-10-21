import { useParams } from "react-router-dom";

import Cabecalho from "../../components/Cabecalho/cabecalho";
import Rodape from "../../components/Rodape/rodape";
import { Title } from "../Homepage/homepage.styles";


function DetalhesEvento() {

    const { id } = useParams();

    return (
        <>

            <Cabecalho />
            <Title>Detalhes do Evento {id}</Title>
            <Rodape />

        </>
    )
}

export default DetalhesEvento