class Api::MessageInputController < ApplicationController

    #skip_before_action :authenticate_request, only: [:create]
    before_action :set_message, only: [:show, :update, :destroy]
    #Get all messages
    def index
        @msgs = MessageInput.all
        render json: @msgs, status: :ok
    end

    #Get a specific message
    def show
        render json: @msg, status: :ok
    end
    
    #Page to create a new message
    def new
        render json: {}, status: :ok
    end

    #Create a new message
    def create
        @msg = MessageInput.new(message_params)
        if @msg.save
            render json: @msg, status: :created
        else
            render json: { errors: @msg.errors.full_messages }, status: :unprocessable_entity
            
        end
    end

    #Edit the message
    def update
        unless @msg.update(message_params)
            render json: { errors: @msg.errors.full_messages }, status: :unprocessable_entity
        end
    end

    #Delete a message
    def destroy
        @msg.destroy
        render json: {}, status: :ok
    end

    private
        def message_params
            params.permit(:uuid, :messages)
        end

        def set_message
            @msg = MessageInput.find([:id])
        end

end