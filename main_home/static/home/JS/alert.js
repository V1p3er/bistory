import react from 'react';
import swal from 'sweetalert';

function app() {
    const showAlert = () => {
        swal({
            title: "completed",
            text: "your suggestion has been send",
            icon: "success",
            button: "Ok",
        });
    };
    return (
        <div>
            <button onClick={showAlert}>send</button>
        </div>
    );
}
export default app;